"""Regression tests for Ableton Live 12 support and version-adaptive extraction.

These run against the sample project under ``data/`` and are skipped automatically
when that file is not available (e.g. in a clean CI checkout).
"""

import pathlib
import unittest

from pyableton import Ableton, extract

DATA_ALS = (
    pathlib.Path(__file__).resolve().parent.parent
    / "data"
    / "uncalled-for-eternal-rest"
    / "Uncalled for the eternal rest.als"
)


@unittest.skipUnless(DATA_ALS.exists(), f"sample Live 12 set not present: {DATA_ALS}")
class TestLive12(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ableton = Ableton(DATA_ALS)
        cls.live_set = extract.find_live_set(cls.ableton.root)

    def test_parses_live_12_header(self):
        # Live 12 renamed several top-level tags; construction must still succeed.
        self.assertTrue(self.ableton.creator.startswith("Ableton Live 12"))
        self.assertIsNotNone(self.ableton.live_set)

    def test_main_track_alias_resolves(self):
        # Live 12 uses <MainTrack>; the alias maps it onto master_track.
        self.assertIsNotNone(self.ableton.live_set.master_track)
        self.assertIsNotNone(extract.find_main_track(self.live_set))

    def test_all_clips_and_window_mapping(self):
        drum = next(
            t for t in extract.iter_midi_tracks(self.live_set)
            if extract.is_drum_track(t)
        )
        self.assertEqual(len(extract.iter_clips(drum)), 9)
        notes = extract.track_notes(drum)
        self.assertEqual(len(notes), 176)  # windowed across all 9 clips
        start, end = extract.track_span(drum)
        self.assertEqual((start, end), (0.0, 96.0))
        # every note lands within the arrangement span
        self.assertTrue(all(0.0 <= beat < 96.0 for beat, *_ in notes))

    def test_tempo_automation(self):
        tempo_map = extract.get_tempo_map(self.live_set)
        self.assertEqual(
            [(b, q) for b, q in tempo_map],
            [(0.0, 140.0), (160.0, 162.0), (448.0, 150.0), (680.0, 140.0)],
        )

    def test_time_signature_automation(self):
        ts_map = extract.get_time_signature_map(self.live_set)
        self.assertEqual(ts_map[0], (0.0, 4, 4))
        meters = {(n, d) for _, n, d in ts_map}
        self.assertIn((7, 4), meters)
        self.assertIn((6, 4), meters)

    def test_arrangement_end_spans_audio(self):
        # The audio track runs far past the drums (full song length).
        self.assertGreater(extract.arrangement_end(self.live_set), 800.0)

    def test_to_muspy_and_midi(self):
        music = self.ableton.to_muspy()
        self.assertGreaterEqual(len(music.tracks), 1)
        self.assertEqual(len(music.tempos), 4)
        self.assertTrue(any(t.is_drum for t in music.tracks))


if __name__ == "__main__":
    unittest.main()
