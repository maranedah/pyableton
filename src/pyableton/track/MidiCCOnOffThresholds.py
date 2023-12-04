from xml.etree import ElementTree

from ..AbletonComponent import AbletonComponent


class MidiCCOnOffThresholds(AbletonComponent):
    min: int
    max: int

    def __init__(self, root: ElementTree.Element):
        super().__init__(root)
