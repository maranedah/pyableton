from xml.etree import ElementTree

from .AbletonComponent import AbletonComponent


class SendPreBool(AbletonComponent):
    id: int
    value: bool

    def __init__(self, root: ElementTree.Element):
        return None
