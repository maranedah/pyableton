import xml.etree.ElementTree as ET

from .AbletonComponent import AbletonComponent
from .LiveSet import LiveSet


class Ableton(AbletonComponent):
    major_version: int
    minor_version: str
    schema_change_count: int
    creator: str
    revision: str
    live_set: LiveSet

    def __init__(self, xml_file: str):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        super().__init__(root)
        # self.major_version = int(root.attrib["MajorVersion"])
        # self.minor_version = root.attrib["MinorVersion"]
        # self.schema_change_count = int(root.attrib["SchemaChangeCount"])
        # self.creator = root.attrib["Creator"]
        # self.revision = root.attrib["Revision"]
        # self.live_set = LiveSet(root.find("LiveSet"))
