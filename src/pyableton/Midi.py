from xml.etree import ElementTree

from .AbletonComponent import AbletonComponent
from .Mixer import Mixer
from .Sequencer import FreezeSequencer, MainSequencer


class MidiName(AbletonComponent):
    effective_name: str
    user_name: str
    annotation: str
    memorized_first_clip_name: str

    def __init__(self, root: ElementTree.Element):
        super().__init__(root)


class AutomationLane(AbletonComponent):
    selected_device: int
    selected_envelope: int
    is_content_selected_in_document: bool
    lane_height: int

    def __init__(self, root: ElementTree.Element):
        super().__init__(root)


class ClipEnvelopeChooserViewState(AbletonComponent):
    selected_device: int
    selected_envelope: int
    prefer_modulation_visible: bool

    def __init__(self, root: ElementTree.Element):
        super().__init__(root)


class MpeSettings(AbletonComponent):
    zone_type: int
    first_note_channel: int
    last_note_channel: int

    def __init__(self, root: ElementTree.Element):
        super().__init__(root)


class IORouting(AbletonComponent):
    target: str
    upper_display_string: str
    lower_display_string: str
    mpe_settings: MpeSettings

    def __init__(self, root: ElementTree.Element):
        super().__init__(root)


class DeviceChain(AbletonComponent):
    # automation_lanes: list[AutomationLane]
    clip_envelope_chooser_view_state: ClipEnvelopeChooserViewState
    audio_input_routing: IORouting
    midi_input_routing: IORouting
    audio_output_routing: IORouting
    midi_output_routing: IORouting
    mixer: Mixer
    main_sequencer: MainSequencer
    freeze_sequencer: FreezeSequencer
    # devices: List[InstrumentGroupDevice]
    # signal_modulations: List[SignalModulation]
    # re_wire_slave_midi_target_id: ReWireSlaveMidiTargetId
    # pitchbend_range: PitchbendRange

    def __init__(self, root: ElementTree.Element):
        super().__init__(root)
