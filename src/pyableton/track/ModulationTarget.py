from xml.etree import ElementTree

from ..AbletonComponent import AbletonComponent


class ModulationTarget(AbletonComponent):
    id: int
    lock_envelope: int

    def __init__(self, root: ElementTree.Element):
        super().__init__(root)
