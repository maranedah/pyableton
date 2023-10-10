from xml.etree import ElementTree

from ..AbletonComponent import AbletonComponent


class TrackDelay(AbletonComponent):
    value: int
    is_value_sample_based: bool

    def __init__(self, root: ElementTree.Element):
        super().__init__(root)
