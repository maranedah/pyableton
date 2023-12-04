from xml.etree import ElementTree

from ..AbletonComponent import AbletonComponent
from .AutomationTarget2 import AutomationTarget2
from .MidiCCOnOffThresholds import MidiCCOnOffThresholds


class On(AbletonComponent):
    lom_id: int
    manual: bool
    automation_target: AutomationTarget2
    midi_CC_on_off_thresholds: MidiCCOnOffThresholds

    def __init__(self, root: ElementTree.Element):
        super().__init__(root)
