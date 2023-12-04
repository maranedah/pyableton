from xml.etree import ElementTree

from ..AbletonComponent import AbletonComponent


class ClipEnvelopeChooserViewState(AbletonComponent):
    selected_device: int
    selected_envelope: int
    prefer_modulation_visible: bool

    def __init__(self, root: ElementTree.Element):
        super().__init__(root)
