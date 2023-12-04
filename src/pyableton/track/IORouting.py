from xml.etree import ElementTree

from ..AbletonComponent import AbletonComponent
from .MpeSettings import MpeSettings


class AudioInputRouting(AbletonComponent):
    target: str
    upper_display_string: str
    lower_display_string: str
    mpe_settings: MpeSettings

    def __init__(self, root: ElementTree.Element):
        super().__init__(root)


class AudioOutputRouting(AbletonComponent):
    target: str
    upper_display_string: str
    lower_display_string: str
    mpe_settings: MpeSettings

    def __init__(self, root: ElementTree.Element):
        super().__init__(root)


class MidiInputRouting(AbletonComponent):
    target: str
    upper_display_string: str
    lower_display_string: str
    mpe_settings: MpeSettings

    def __init__(self, root: ElementTree.Element):
        super().__init__(root)


class MidiOutputRouting(AbletonComponent):
    target: str
    upper_display_string: str
    lower_display_string: str
    mpe_settings: MpeSettings

    def __init__(self, root: ElementTree.Element):
        super().__init__(root)
