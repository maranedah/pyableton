import pathlib
import unittest

from pyableton.Ableton import Ableton
from pyableton.AbletonComponent import AbletonComponent
from pyableton.LiveSet import LiveSet
from pyableton.Track import Track


class TestAbleton(unittest.TestCase):
    def setUp(self):
        test_path = pathlib.Path(__file__).parent
        self.ableton = Ableton(test_path / "evasiva.xml")
        self.live_set = self.ableton.live_set

    def test_ableton_object(self):
        assert self.ableton.major_version == 5
        assert self.ableton.minor_version == "11.0_11300"
        assert self.ableton.schema_change_count == 3
        assert self.ableton.creator == "Ableton Live 11.3.3"
        assert self.ableton.revision == "d46a6d1068bab7b392804ef645e6a9bbc2eb0b27"
        assert isinstance(self.ableton.live_set, AbletonComponent)
        assert isinstance(self.ableton.live_set, LiveSet)

    def test_live_set(self):
        assert self.live_set.next_pointee_id == 27102
        assert self.live_set.overwrite_protection_number == 2819
        assert self.live_set.lom_id == 3
        assert self.live_set.lom_id_view == 0
        assert isinstance(self.live_set.tracks, list)
        assert all(isinstance(element, Track) for element in self.live_set.tracks)
        assert len(self.live_set.tracks) == 6
        # assert isinstance(self.live_set.master_track, MasterTrack)

    def test_to_als(self):
        return None

    def test_to_xml(self):
        return None

    def test_midi_tracks(self):
        assert self.ableton.live_set.tracks[0] is not None


if __name__ == "__main__":
    unittest.main()
