import pathlib
import unittest

from pyableton.Ableton import Ableton


class TestAbleton(unittest.TestCase):
    def setUp(self):
        test_path = pathlib.Path(__file__).parent
        self.ableton = Ableton(test_path / "evasiva.xml")

    def test_to_als(self):
        return None

    def test_to_xml(self):
        return None

    def test_has_live_set(self):
        assert self.ableton.live_set is not None


if __name__ == "__main__":
    unittest.main()
