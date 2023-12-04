from xml.etree import ElementTree

from ..AbletonComponent import AbletonComponent


class MpeSettings(AbletonComponent):
    zone_type: int
    first_note_channel: int
    last_note_channel: int

    def __init__(self, root: ElementTree.Element):
        super().__init__(root)
