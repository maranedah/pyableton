from xml.etree import ElementTree

from ..AbletonComponent import AbletonComponent


class AutomationLane(AbletonComponent):
    selected_device: int
    selected_envelope: int
    is_content_selected_in_document: bool
    lane_height: int

    def __init__(self, root: ElementTree.Element):
        super().__init__(root)
