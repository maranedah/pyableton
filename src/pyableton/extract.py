"""Version-adaptive extraction helpers.

These functions read tempo, time-signature and note data straight from the parsed
Ableton Live Set XML tree (``xml.etree.ElementTree``), rather than relying on the
reflective typed model. That keeps MIDI export robust across Ableton Live versions
whose schemas differ (e.g. Live 11 ``MasterTrack`` vs Live 12 ``MainTrack``), and it
reads *all* arrangement clips and the *full* tempo / time-signature automation instead
of only the first clip and a single manual tempo.

All times returned by these helpers are in Ableton beats (quarter notes), matching the
units used by clip ``CurrentStart`` / ``CurrentEnd`` and automation event ``Time``.
"""

import re

from .constants import TIME_SIGNATURE_IDS

# Ableton stores the "value at the very start of the song" as an automation event with
# this sentinel time. It should be treated as beat 0.
TIMELINE_START_SENTINEL = -63072000.0

_DRUM_NAME_RE = re.compile(r"drum|kit|perc", re.IGNORECASE)


def _value(element, path, cast=None, default=None):
    """Return the ``Value`` attribute of ``element.find(path)``, optionally cast."""
    if element is None:
        return default
    node = element.find(path)
    if node is None or "Value" not in node.attrib:
        return default
    raw = node.attrib["Value"]
    if cast is None:
        return raw
    try:
        return cast(raw)
    except (ValueError, TypeError):
        return default


def find_live_set(root):
    """Return the ``<LiveSet>`` element from the document root."""
    if root is None:
        return None
    if root.tag == "LiveSet":
        return root
    return root.find("LiveSet")


def find_main_track(live_set):
    """Return the master/main track element, tolerating the Live 11/12 rename."""
    if live_set is None:
        return None
    for tag in ("MasterTrack", "MainTrack"):
        element = live_set.find(tag)
        if element is not None:
            return element
    return None


def iter_midi_tracks(live_set):
    """Return all ``<MidiTrack>`` elements in document (track) order."""
    tracks = live_set.find("Tracks") if live_set is not None else None
    if tracks is None:
        return []
    return [track for track in tracks if track.tag == "MidiTrack"]


def track_name(track_element):
    """Return the track's effective (falling back to user) name."""
    name = _value(track_element, "Name/EffectiveName")
    if name is None:
        name = _value(track_element, "Name/UserName")
    return name or ""


def iter_clips(track_element):
    """Return the arrangement MIDI clips of a track, in timeline order."""
    events = track_element.find(
        "DeviceChain/MainSequencer/ClipTimeable/ArrangerAutomation/Events"
    )
    if events is None:
        return []
    return [clip for clip in events if clip.tag == "MidiClip"]


def is_drum_track(track_element):
    """Heuristically decide whether a MIDI track is a drum/percussion track."""
    if _DRUM_NAME_RE.search(track_name(track_element)):
        return True
    for clip in iter_clips(track_element):
        if _DRUM_NAME_RE.search(_value(clip, "Name", default="") or ""):
            return True
    return False


def track_span(track_element):
    """Return ``(start_beat, end_beat)`` covering all of the track's clips."""
    starts, ends = [], []
    for clip in iter_clips(track_element):
        start = _value(clip, "CurrentStart", float)
        end = _value(clip, "CurrentEnd", float)
        if start is not None:
            starts.append(start)
        if end is not None:
            ends.append(end)
    if not starts or not ends:
        return (0.0, 0.0)
    return (min(starts), max(ends))


def arrangement_end(live_set):
    """Return the last arrangement beat used by any clip (MIDI or audio).

    This spans the whole song (e.g. the full length of an audio track), not just the
    MIDI content, so a score can be extended to the true end of the arrangement.
    """
    end = 0.0
    tracks = live_set.find("Tracks") if live_set is not None else None
    if tracks is None:
        return end
    for track in tracks:
        for current_end in track.iter("CurrentEnd"):
            try:
                end = max(end, float(current_end.attrib.get("Value")))
            except (TypeError, ValueError):
                continue
    return end


def clip_notes(clip_element):
    """Yield ``(beat, pitch, duration, velocity)`` for one arrangement clip.

    Each note is stored in the clip's own *content* timeline. Only notes inside the
    played window ``[LoopStart, LoopEnd)`` sound in the arrangement; they are mapped to
    absolute arrangement beats via ``arr = CurrentStart + (time - LoopStart)`` and their
    durations are clipped so they do not spill past the window end.
    """
    current_start = _value(clip_element, "CurrentStart", float, 0.0)
    current_end = _value(clip_element, "CurrentEnd", float, current_start)
    loop_start = _value(clip_element, "Loop/LoopStart", float, current_start)
    loop_end = _value(clip_element, "Loop/LoopEnd", float, current_end)

    notes = []
    for key_track in clip_element.findall("Notes/KeyTracks/KeyTrack"):
        pitch = _value(key_track, "MidiKey", int)
        if pitch is None:
            continue
        for event in key_track.findall("Notes/MidiNoteEvent"):
            if event.attrib.get("IsEnabled", "true") == "false":
                continue
            time = float(event.attrib.get("Time", "0"))
            if time < loop_start or time >= loop_end:
                continue  # outside the played window -> silent in the arrangement
            duration = float(event.attrib.get("Duration", "0"))
            velocity = float(event.attrib.get("Velocity", "100"))
            arrangement_beat = current_start + (time - loop_start)
            duration = min(duration, loop_end - time)
            notes.append((arrangement_beat, pitch, duration, velocity))
    return notes


def track_notes(track_element):
    """Return all arrangement notes of a track, sorted by ``(beat, pitch)``."""
    notes = []
    for clip in iter_clips(track_element):
        notes.extend(clip_notes(clip))
    notes.sort(key=lambda note: (note[0], note[1]))
    return notes


def _automation_events_for_target(main_track, target_id):
    """Return automation event elements for the envelope pointing at ``target_id``."""
    if main_track is None or target_id is None:
        return []
    for envelope in main_track.findall(
        "AutomationEnvelopes/Envelopes/AutomationEnvelope"
    ):
        pointee = envelope.find("EnvelopeTarget/PointeeId")
        if pointee is not None and pointee.attrib.get("Value") == target_id:
            events = envelope.find("Automation/Events")
            if events is not None:
                return list(events)
    return []


def _dedupe(sorted_changes):
    """Collapse events sharing a beat (last wins) and drop repeated values."""
    by_beat = {}
    for beat, value in sorted_changes:
        by_beat[beat] = value  # later document-order event at a beat wins
    result = []
    for beat in sorted(by_beat):
        value = by_beat[beat]
        if not result or result[-1][1] != value:
            result.append((beat, value))
    return result


def get_tempo_map(live_set):
    """Return sorted ``[(beat, qpm)]`` tempo changes, or the manual tempo as fallback."""
    main_track = find_main_track(live_set)
    mixer = main_track.find("DeviceChain/Mixer") if main_track is not None else None
    manual = _value(mixer, "Tempo/Manual", float)
    target_id = None
    if mixer is not None:
        node = mixer.find("Tempo/AutomationTarget")
        target_id = node.attrib.get("Id") if node is not None else None

    changes = []
    for event in _automation_events_for_target(main_track, target_id):
        beat = max(0.0, float(event.attrib.get("Time", "0")))
        qpm = float(event.attrib.get("Value"))
        changes.append((beat, qpm))

    if not changes:
        return [(0.0, manual if manual is not None else 120.0)]
    return _dedupe(changes)


def get_time_signature_map(live_set):
    """Return sorted ``[(beat, numerator, denominator)]`` meter changes.

    Falls back to the mixer's manual time signature, then to 4/4.
    """
    main_track = find_main_track(live_set)
    mixer = main_track.find("DeviceChain/Mixer") if main_track is not None else None
    manual_enum = _value(mixer, "TimeSignature/Manual", int)
    target_id = None
    if mixer is not None:
        node = mixer.find("TimeSignature/AutomationTarget")
        target_id = node.attrib.get("Id") if node is not None else None

    changes = []
    for event in _automation_events_for_target(main_track, target_id):
        signature = TIME_SIGNATURE_IDS.get(int(event.attrib.get("Value")))
        if signature is None:
            continue
        beat = max(0.0, float(event.attrib.get("Time", "0")))
        changes.append((beat, (signature["numerator"], signature["denominator"])))

    if not changes:
        signature = TIME_SIGNATURE_IDS.get(manual_enum) if manual_enum else None
        if signature is None:
            signature = {"numerator": 4, "denominator": 4}
        return [(0.0, signature["numerator"], signature["denominator"])]

    return [(beat, num, den) for beat, (num, den) in _dedupe(changes)]
