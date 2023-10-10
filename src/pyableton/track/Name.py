from xml.etree import ElementTree

from ..AbletonComponent import AbletonComponent


class Name(AbletonComponent):
    effective_name: str
    user_name: str
    annotation: str
    memorized_first_clip_name: str

    def __init__(self, root: ElementTree.Element):
        super().__init__(root)
