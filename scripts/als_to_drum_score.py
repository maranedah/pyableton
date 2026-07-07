"""Extract a drum track from an Ableton Live Set and render it as a drum sheet PDF.

Pipeline
--------
1. Parse the ``.als`` with :class:`pyableton.Ableton` (version-adaptive).
2. Pull every arrangement clip of the drum track, mapped onto the arrangement
   timeline (see :func:`pyableton.extract.clip_notes`).
3. Read the full tempo and time-signature automation maps.
4. Render the drums across the *entire* arrangement span so that tempo changes and
   meter changes are shown, even where they fall after the last drum note (empty
   bars become multi-measure rests). Onsets are quantised to a 1/16 grid.
5. Write a standard MIDI byproduct and a LilyPond ``.ly`` file, then invoke
   ``lilypond`` to produce the PDF.

Usage
-----
    python scripts/als_to_drum_score.py [--als PATH] [--track SUBSTR]
        [--out-dir DIR] [--title TITLE] [--no-pdf]
"""

import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path

# Make `pyableton` importable when run straight from the repo (src/ layout).
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

import muspy  # noqa: E402
from pyableton import Ableton, extract  # noqa: E402

DEFAULT_ALS = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "uncalled-for-eternal-rest"
    / "Uncalled for the eternal rest.als"
)

CELLS_PER_QUARTER = 4  # 1/16-note quantisation grid

# General-MIDI percussion key -> LilyPond drummode note name.
GM_TO_LILY = {
    35: "bda",   # Acoustic Bass Drum
    36: "bd",    # Bass Drum 1
    37: "ss",    # Side Stick
    38: "sn",    # Acoustic Snare
    39: "cb",    # Hand Clap -> cowbell notehead (closest available voice)
    40: "sn",    # Electric Snare
    41: "tomfl", # Low Floor Tom
    42: "hh",    # Closed Hi-Hat
    43: "tomfh", # High Floor Tom
    44: "hhp",   # Pedal Hi-Hat
    45: "toml",  # Low Tom
    46: "hho",   # Open Hi-Hat
    47: "tomml", # Low-Mid Tom
    48: "tommh", # Hi-Mid Tom
    49: "cymc",  # Crash Cymbal 1
    50: "tomh",  # High Tom
    51: "cymr",  # Ride Cymbal 1
    52: "cymc",  # China -> crash
    53: "cymr",  # Ride Bell -> ride
    54: "tamb",  # Tambourine
    55: "cymc",  # Splash -> crash
    56: "cb",    # Cowbell
    57: "cymc",  # Crash 2 -> crash
    59: "cymr",  # Ride 2 -> ride
}

# Cell length (in 1/16 cells) -> LilyPond duration digit.
CELL_TO_DURATION = {16: "1", 8: "2", 4: "4", 2: "8", 1: "16"}
_POWERS = (16, 8, 4, 2, 1)


def duration_tokens(position, length):
    """Decompose a span into metrically-aligned power-of-two note values.

    ``position`` and ``length`` are in 1/16 cells. Returns a list of LilyPond duration
    digits which, tied together, notate a single event of ``length`` cells starting at
    ``position`` within its measure.
    """
    tokens = []
    pos, remaining = position, length
    while remaining > 0:
        for cells in _POWERS:
            if cells <= remaining and pos % cells == 0:
                tokens.append(CELL_TO_DURATION[cells])
                pos += cells
                remaining -= cells
                break
        else:  # pragma: no cover - defensive; alignment always allows 1 cell
            tokens.append("16")
            pos += 1
            remaining -= 1
    return tokens


def active_at(beat, changes):
    """Return the value of a change list ``[(beat, value...)]`` active at ``beat``."""
    current = changes[0][1:]
    for entry in changes:
        if entry[0] <= beat + 1e-9:
            current = entry[1:]
        else:
            break
    return current


def build_grid(notes):
    """Map quantised onset cell -> set of LilyPond drum names, plus report drops."""
    grid = {}
    unmapped = set()
    for beat, pitch, _duration, _velocity in notes:
        name = GM_TO_LILY.get(int(pitch))
        if name is None:
            unmapped.add(int(pitch))
            name = "sn"  # fall back to snare line so nothing is silently lost
        cell = int(round(beat * CELLS_PER_QUARTER))
        grid.setdefault(cell, set()).add(name)
    return grid, unmapped


def render_bar(grid, bar_start_cell, bar_cells):
    """Return LilyPond tokens for one measure given the onset grid."""
    onsets = {
        c: grid[bar_start_cell + c]
        for c in range(bar_cells)
        if (bar_start_cell + c) in grid
    }
    if not onsets:
        return None  # signal an empty bar (caller emits a multi-measure rest)

    tokens = []
    cell = 0
    onset_cells = sorted(onsets)
    while cell < bar_cells:
        if cell in onsets:
            names = " ".join(sorted(onsets[cell]))
            nxt = next((oc for oc in onset_cells if oc > cell), bar_cells)
            durations = duration_tokens(cell, nxt - cell)
            for i, dur in enumerate(durations):
                tie = "~" if i < len(durations) - 1 else ""
                tokens.append(f"<{names}>{dur}{tie}")
            cell = nxt
        else:
            nxt = next((oc for oc in onset_cells if oc > cell), bar_cells)
            for dur in duration_tokens(cell, nxt - cell):
                tokens.append(f"r{dur}")
            cell = nxt
    return " ".join(tokens)


def build_lilypond(notes, tempo_map, ts_map, span_end_beat, title, subtitle):
    """Build the full LilyPond document string for the drum score."""
    grid, unmapped = build_grid(notes)

    # Extend to a whole number of measures covering the last tempo/meter change too.
    last_change = max(
        span_end_beat,
        tempo_map[-1][0] if tempo_map else 0,
        ts_map[-1][0] if ts_map else 0,
    )

    body = []
    current_meter = None
    current_tempo = None
    # Runs of consecutive empty measures (same meter, no tempo/meter change) are
    # collapsed into one multi-measure rest so the tail of the piece stays compact
    # while every tempo / time-signature change remains visible.
    empty_run = 0
    empty_run_meter = None

    def flush_empty():
        nonlocal empty_run, empty_run_meter
        if empty_run:
            num, den = empty_run_meter
            body.append(f"  R1*{num * empty_run}/{den}")
            empty_run = 0
            empty_run_meter = None

    bar_start_beat = 0.0
    guard = 0
    while bar_start_beat <= last_change + 1e-6:
        guard += 1
        if guard > 20000:  # pragma: no cover - runaway guard
            break
        num, den = active_at(bar_start_beat, ts_map)
        (qpm,) = active_at(bar_start_beat, tempo_map)

        if (num, den) != current_meter or qpm != current_tempo:
            flush_empty()  # a change ends the current rest run
        if (num, den) != current_meter:
            body.append(f"  \\time {num}/{den}")
            current_meter = (num, den)
        if qpm != current_tempo:
            body.append(f"  \\tempo 4 = {int(round(qpm))}")
            current_tempo = qpm

        bar_len_beats = num * 4.0 / den
        bar_cells = int(round(bar_len_beats * CELLS_PER_QUARTER))
        bar_start_cell = int(round(bar_start_beat * CELLS_PER_QUARTER))
        rendered = render_bar(grid, bar_start_cell, bar_cells)

        if rendered is None:
            if empty_run and empty_run_meter != (num, den):
                flush_empty()
            empty_run += 1
            empty_run_meter = (num, den)
        else:
            flush_empty()
            body.append(f"  {rendered}  |")

        bar_start_beat += bar_len_beats

    flush_empty()

    music = "\n".join(body)
    doc = f"""\\version "2.24.0"

\\header {{
  title = "{title}"
  subtitle = "{subtitle}"
  tagline = ##f
}}

\\score {{
  \\new DrumStaff \\with {{
    instrumentName = "Drums"
  }} \\drummode {{
    \\compressMMRests {{
{music}
    }}
  }}
  \\layout {{ }}
}}
"""
    return doc, unmapped


def write_midi(ableton, track_element, tempo_map, ts_map, midi_path):
    """Write a standard MIDI file containing only the drum track."""
    resolution = muspy.DEFAULT_RESOLUTION

    def ticks(beat):
        return int(round(beat * resolution))

    notes = [
        muspy.Note(
            time=ticks(beat),
            pitch=int(pitch),
            duration=max(1, ticks(duration)),
            velocity=max(0, min(127, int(round(velocity)))),
        )
        for beat, pitch, duration, velocity in extract.track_notes(track_element)
    ]
    music = muspy.Music(
        resolution=resolution,
        tempos=[muspy.Tempo(time=ticks(b), qpm=q) for b, q in tempo_map],
        time_signatures=[
            muspy.TimeSignature(time=ticks(b), numerator=n, denominator=d)
            for b, n, d in ts_map
        ],
        tracks=[
            muspy.Track(
                program=0,
                is_drum=True,
                name=extract.track_name(track_element),
                notes=notes,
            )
        ],
    )
    music.write_midi(str(midi_path))
    return len(notes)


def find_lilypond():
    """Locate the lilypond executable on PATH or in common Windows install dirs."""
    found = shutil.which("lilypond")
    if found:
        return found
    candidates = []
    for base in (
        os.environ.get("LOCALAPPDATA", ""),
        os.environ.get("ProgramFiles", ""),
        os.environ.get("ProgramFiles(x86)", ""),
    ):
        if base:
            candidates.extend(Path(base).glob("**/lilypond*/bin/lilypond.exe"))
    return str(candidates[0]) if candidates else None


def select_drum_track(live_set, track_substr):
    """Return the drum track element to render, honouring an optional name filter."""
    midi_tracks = extract.iter_midi_tracks(live_set)
    if track_substr:
        for track in midi_tracks:
            if track_substr.lower() in extract.track_name(track).lower():
                return track
        raise SystemExit(f"No MIDI track matching {track_substr!r} was found.")
    for track in midi_tracks:
        if extract.is_drum_track(track) and extract.track_notes(track):
            return track
    # fall back to the track with the most notes
    with_notes = [(len(extract.track_notes(t)), t) for t in midi_tracks]
    with_notes.sort(key=lambda item: item[0], reverse=True)
    if with_notes and with_notes[0][0] > 0:
        return with_notes[0][1]
    raise SystemExit("No MIDI track with notes was found in the set.")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--als", type=Path, default=DEFAULT_ALS, help="Path to .als")
    parser.add_argument(
        "--track", default=None, help="Substring of the drum track name (optional)"
    )
    parser.add_argument("--out-dir", type=Path, default=None, help="Output directory")
    parser.add_argument("--title", default="Uncalled-For the Eternal Rest")
    parser.add_argument("--no-pdf", action="store_true", help="Skip LilyPond render")
    args = parser.parse_args(argv)

    als_path = args.als
    if not als_path.exists():
        raise SystemExit(f"ALS file not found: {als_path}")
    out_dir = args.out_dir or als_path.parent
    out_dir.mkdir(parents=True, exist_ok=True)
    stem = "Uncalled-For-drums"

    print(f"Parsing {als_path.name} ...")
    ableton = Ableton(als_path)
    print(f"  Ableton creator: {ableton.creator}")
    live_set = extract.find_live_set(ableton.root)

    track = select_drum_track(live_set, args.track)
    notes = extract.track_notes(track)
    span = extract.track_span(track)
    tempo_map = extract.get_tempo_map(live_set)
    ts_map = extract.get_time_signature_map(live_set)
    # Extend the score to the full arrangement length (e.g. the audio track), so the
    # sheet runs to the end of the song and shows every tempo/meter change.
    arrangement_end = extract.arrangement_end(live_set)
    song_end = max(span[1], arrangement_end)

    print(f"  Drum track: {extract.track_name(track)!r}")
    print(f"  Clips: {len(extract.iter_clips(track))}  played notes: {len(notes)}")
    print(f"  Drum span (beats): {span[0]:.1f} -> {span[1]:.1f}")
    print(f"  Arrangement end (beats): {arrangement_end:.1f}")
    print(f"  Tempo changes: {[(b, q) for b, q in tempo_map]}")
    print(f"  Time-signature changes: {len(ts_map)} "
          f"(first: {ts_map[0][1]}/{ts_map[0][2]}, "
          f"last change at beat {ts_map[-1][0]:.0f} -> {ts_map[-1][1]}/{ts_map[-1][2]})")

    # MIDI byproduct (the literal extracted MIDI).
    midi_path = out_dir / f"{stem}.mid"
    n_written = write_midi(ableton, track, tempo_map, ts_map, midi_path)
    print(f"  Wrote MIDI: {midi_path}  ({n_written} notes)")

    # LilyPond score spanning the whole arrangement (so changes are visible).
    subtitle = "Drum score - tempo & meter changes reflected"
    doc, unmapped = build_lilypond(
        notes, tempo_map, ts_map, song_end, args.title, subtitle
    )
    if unmapped:
        print(f"  NOTE: unmapped GM keys folded onto snare: {sorted(unmapped)}")
    ly_path = out_dir / f"{stem}.ly"
    ly_path.write_text(doc, encoding="utf-8")
    print(f"  Wrote LilyPond: {ly_path}")

    if args.no_pdf:
        return 0

    lilypond = find_lilypond()
    if not lilypond:
        print("  LilyPond not found on PATH; skipping PDF. Install it or run "
              "lilypond manually on the .ly file.")
        return 0

    print(f"  Rendering PDF with {lilypond} ...")
    result = subprocess.run(
        [lilypond, "-o", str(out_dir / stem), str(ly_path)],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        print(result.stdout)
        print(result.stderr)
        raise SystemExit(f"LilyPond failed (exit {result.returncode}).")
    pdf_path = out_dir / f"{stem}.pdf"
    print(f"  Done: {pdf_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
