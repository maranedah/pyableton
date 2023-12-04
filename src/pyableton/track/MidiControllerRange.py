from xml.etree import ElementTree

from ..AbletonComponent import AbletonComponent


class MidiControllerRange(AbletonComponent):
    min: float
    max: float

    def __init__(self, root: ElementTree.Element):
        super().__init__(root)
