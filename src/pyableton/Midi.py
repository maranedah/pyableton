from .AbletonComponent import AbletonComponent
from .Mixer import Mixer
from .Sequencer import FreezeSequencer, MainSequencer


class MidiName(AbletonComponent):
    """
    MidiName Class

    Represents MIDI name information in Ableton Live.

    Attributes
    ----------
    effective_name : str
        The effective name for MIDI in Ableton Live.
    user_name : str
        The user-defined name for MIDI in Ableton Live.
    annotation : str
        Annotation information for MIDI in Ableton Live.
    memorized_first_clip_name : str
        The memorized first clip name for MIDI in Ableton Live.

    """

    effective_name: str
    user_name: str
    annotation: str
    memorized_first_clip_name: str


class AutomationLane(AbletonComponent):
    """
    AutomationLane Class

    Represents an automation lane in Ableton Live.

    Attributes
    ----------
    selected_device : int
        The selected device for the automation lane.
    selected_envelope : int
        The selected envelope for the automation lane.
    is_content_selected_in_document : bool
        Flag indicating whether content is selected in the document.
    lane_height : int
        The height of the automation lane.

    """

    selected_device: int
    selected_envelope: int
    is_content_selected_in_document: bool
    lane_height: int


class ClipEnvelopeChooserViewState(AbletonComponent):
    """
    ClipEnvelopeChooserViewState Class

    Represents the view state of the clip envelope chooser in Ableton Live.

    Attributes
    ----------
    selected_device : int
        The selected device for the clip envelope chooser.
    selected_envelope : int
        The selected envelope for the clip envelope chooser.
    prefer_modulation_visible : bool
        Flag indicating whether modulation visibility is preferred.

    """

    selected_device: int
    selected_envelope: int
    prefer_modulation_visible: bool


class MpeSettings(AbletonComponent):
    """
    MpeSettings Class

    Represents MPE (MIDI Polyphonic Expression) settings in Ableton Live.

    Attributes
    ----------
    zone_type : int
        The type of MPE zone.
    first_note_channel : int
        The first MIDI note channel.
    last_note_channel : int
        The last MIDI note channel.

    """

    zone_type: int
    first_note_channel: int
    last_note_channel: int


class IORouting(AbletonComponent):
    """
    IORouting Class

    Represents input/output routing information in Ableton Live.

    Attributes
    ----------
    target : str
        The routing target.
    upper_display_string : str
        The upper display string.
    lower_display_string : str
        The lower display string.
    mpe_settings : MpeSettings
        MPE settings associated with the routing.

    """

    target: str
    upper_display_string: str
    lower_display_string: str
    mpe_settings: MpeSettings


class DeviceChain(AbletonComponent):
    """
    DeviceChain Class

    Represents a device chain in Ableton Live.

    Attributes
    ----------
    clip_envelope_chooser_view_state : ClipEnvelopeChooserViewState
        View state of the clip envelope chooser.
    audio_input_routing : IORouting
        Audio input routing information.
    midi_input_routing : IORouting
        MIDI input routing information.
    audio_output_routing : IORouting
        Audio output routing information.
    midi_output_routing : IORouting
        MIDI output routing information.
    mixer : Mixer
        Mixer information.
    main_sequencer : MainSequencer
        Main sequencer information.
    freeze_sequencer : FreezeSequencer
        Freeze sequencer information.

    """

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
