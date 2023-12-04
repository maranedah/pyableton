from xml.etree import ElementTree

from ..AbletonComponent import AbletonComponent
from .AutomationTarget import AutomationTarget
from .MidiControllerRange import MidiControllerRange
from .ModulationTarget import ModulationTarget


class Pan(AbletonComponent):
    lom_id: int
    manual: int
    midi_controller_range: MidiControllerRange
    automation_target: AutomationTarget
    modulation_target: ModulationTarget

    def __init__(self, root: ElementTree.Element):
        super().__init__(root)
