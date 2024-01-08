from xml.etree import ElementTree

from .AbletonComponent import AbletonComponent
from .Midi import DeviceChain, MidiName


class Track(AbletonComponent):
    """
    Track Class

    Represents a track in Ableton Live.

    Attributes
    ----------
    (Specific attributes for MidiTrack and ReturnTrack subclasses)

    Methods
    -------
    __new__(cls, track_node: ElementTree.Element)
        Factory method to create either a MidiTrack or ReturnTrack instance based on the XML node.

    """

    def __new__(cls, track_node):
        if cls is Track:
            if track_node.tag == "MidiTrack":
                return MidiTrack(track_node)
            elif track_node.tag == "ReturnTrack":
                return ReturnTrack(track_node)
            else:
                raise ValueError(f"Unknown species: {track_node}")
        else:
            return super().__new__(cls)


class TrackDelay(AbletonComponent):
    """
    TrackDelay Class

    Represents track delay settings in Ableton Live.

    Attributes
    ----------
    value : int
        The delay value.
    is_value_sample_based : bool
        Flag indicating whether the delay value is sample-based.

    """

    value: int
    is_value_sample_based: bool


class MidiTrack(Track):
    """
    MidiTrack Class

    Represents a MIDI track in Ableton Live.

    Attributes
    ----------
    id : int
        Unique identifier for the MIDI track.
    lom_id : int
        LOM (Live Object Model) identifier for the MIDI track.
    lom_id_view : int
        LOM identifier for the view of the MIDI track.
    is_content_selected_in_document : bool
        Flag indicating whether the MIDI track's content is selected in the document.
    preferred_content_view_mode : int
        Preferred content view mode for the MIDI track.
    track_delay : TrackDelay
        Track delay settings for the MIDI track.
    name : MidiName
        Name settings for the MIDI track.
    color : int
        Color code for the MIDI track.
    track_group_id : int
        Identifier for the track group to which the MIDI track belongs.
    track_unfolded : bool
        Flag indicating whether the MIDI track is unfolded.
    devices_list_wrapper : int
        Wrapper for the list of devices associated with the MIDI track.
    clip_slots_list_wrapper : int
        Wrapper for the list of clip slots associated with the MIDI track.
    view_data : dict
        Dictionary containing view-related data for the MIDI track.
    linked_track_group_id : int
        Identifier for the linked track group.
    saved_playing_slot : int
        Identifier for the saved playing slot.
    saved_playing_offset : int
        Offset value for the saved playing slot.
    freeze : bool
        Flag indicating whether the MIDI track is frozen.
    velocity_detail : int
        Detail level for velocity settings.
    need_arranger_refreeze : bool
        Flag indicating whether refreezing is needed in the arranger.
    post_process_freeze_clips : int
        Number of clips to post-process during freezing.
    device_chain : DeviceChain
        Device chain settings for the MIDI track.
    re_wire_slave_midi_target_id : int
        Identifier for the ReWire slave MIDI target.
    pitchbend_range : int
        Pitchbend range value for the MIDI track.

    """

    id: int
    lom_id: int
    lom_id_view: int
    is_content_selected_in_document: bool
    preferred_content_view_mode: int
    track_delay: TrackDelay
    name: MidiName
    color: int
    # automation_envelopes: List[Envelope]
    track_group_id: int
    track_unfolded: bool
    devices_list_wrapper: int
    clip_slots_list_wrapper: int
    view_data: dict
    # take_lanes: list[TakeLane]
    linked_track_group_id: int
    saved_playing_slot: int
    saved_playing_offset: int
    freeze: bool
    velocity_detail: int
    need_arranger_refreeze: bool
    post_process_freeze_clips: int
    device_chain: DeviceChain
    re_wire_slave_midi_target_id: int
    pitchbend_range: int


class ReturnTrack(Track):
    """
    ReturnTrack Class

    Represents a return track in Ableton Live.

    Attributes
    ----------
    id : int
        Unique identifier for the return track.
    lom_id : int
        LOM (Live Object Model) identifier for the return track.
    lom_id_view : int
        LOM identifier for the view of the return track.
    is_content_selected_in_document : bool
        Flag indicating whether the return track's content is selected in the document.
    preferred_content_view_mode : int
        Preferred content view mode for the return track.
    color : int
        Color code for the return track.
    track_group_id : int
        Identifier for the track group to which the return track belongs.
    track_unfolded : bool
        Flag indicating whether the return track is unfolded.
    devices_list_wrapper : int
        Wrapper for the list of devices associated with the return track.
    clip_slots_list_wrapper : int
        Wrapper for the list of clip slots associated with the return track.
    view_data : dict
        Dictionary containing view-related data for the return track.
    linked_track_group_id : int
        Identifier for the linked track group.
    device_chain : DeviceChain
        Device chain settings for the return track.

    """

    id: int
    lom_id: int
    lom_id_view: int
    is_content_selected_in_document: bool
    preferred_content_view_mode: int
    # track_delay: TrackDelay
    # name: Name
    color: int
    # automation_envelopes: List[Envelope]
    track_group_id: int
    track_unfolded: bool
    devices_list_wrapper: int
    clip_slots_list_wrapper: int
    view_data: dict
    # take_lanes: list[TakeLane]
    linked_track_group_id: int
    # device_chain: DeviceChain


class TracksListWrapper(AbletonComponent):
    """
    TracksListWrapper Class

    Wrapper for a list of tracks in Ableton Live.

    Attributes
    ----------
    None

    """

    def __init__(self, root: ElementTree.Element):
        return None


class VisibleTracksListWrapper(AbletonComponent):
    """
    VisibleTracksListWrapper Class

    Wrapper for a list of visible tracks in Ableton Live.

    """

    def __init__(self, root: ElementTree.Element):
        return None


class Tempo(AbletonComponent):
    """
    Tempo Class

    Represents tempo settings in Ableton Live.

    Attributes
    ----------
    lom_id : int
        LOM identifier for the tempo settings.
    manual : int
        Manual setting for the tempo.

    Methods
    -------
    None

    """

    lom_id: int
    manual: int
    # midi_controller_range
    # automation_target
    # modulation_target


class MasterTrackMixer(AbletonComponent):
    """
    MasterTrackMixer Class

    Represents the mixer settings for the master track in Ableton Live.

    Attributes
    ----------
    lom_id : int
        LOM identifier for the master track mixer settings.
    lom_id_view : int
        LOM identifier for the view of the master track mixer.
    is_expanded : bool
        Flag indicating whether the master track mixer is expanded.
    modulation_source_count : int
        Count of modulation sources for the master track mixer.
    parameters_list_wrapper : int
        Wrapper for the list of parameters associated with the master track mixer.
    pointee : int
        Pointee value for the master track mixer.
    last_selected_timeable_index : int
        Index of the last selected timeable item in the master track mixer.
    last_selected_clip_envelope_index : int
        Index of the last selected clip envelope in the master track mixer.
    is_folded : bool
        Flag indicating whether the master track mixer is folded.
    should_show_preset_name : bool
        Flag indicating whether the preset name should be shown for the master track mixer.
    user_name : str
        User name for the master track mixer.
    annotation : str
        Annotation for the master track mixer.
    solo_sink : bool
        Flag indicating whether the solo sink is enabled.
    pan_mode : int
        Pan mode for the master track mixer.
    view_state_sesstion_track_width : int
        View state session track width for the master track mixer.
    sends_list_wrapper : int
        Wrapper for the list of sends associated with the master track mixer.
    tempo : Tempo
        Tempo settings for the master track mixer.
    tempo_automation_view_bottom : int
        Bottom view position for tempo automation in the master track mixer.
    tempo_automation_view_top : int
        Top view position for tempo automation in the master track mixer.

    """

    lom_id: int
    lom_id_view: int
    is_expanded: bool
    # on:
    modulation_source_count: int
    parameters_list_wrapper: int
    pointee: int
    last_selected_timeable_index: int
    last_selected_clip_envelope_index: int
    # last_preset_ref
    # locked_scripts
    is_folded: bool
    should_show_preset_name: bool
    user_name: str
    annotation: str
    # source_context
    # sends:
    # speaker: Speaker
    solo_sink: bool
    pan_mode: int
    # pan: Pan
    # split_stereo_pan_l:
    # split_stereo_pan_r:
    # volume:
    view_state_sesstion_track_width: int
    # cross_fade_state
    sends_list_wrapper: int
    tempo: Tempo
    # time_signature: TimeSignature
    # global_groove_amount:
    # cross_fade:
    tempo_automation_view_bottom: int
    tempo_automation_view_top: int


class MasterTrackDeviceChain(AbletonComponent):
    """
    MasterTrackDeviceChain Class

    Represents the device chain settings for the master track in Ableton Live.

    Attributes
    ----------
    mixer : MasterTrackMixer
        Master track mixer settings for the device chain.

    """

    # automation_lanes: AutomationLanes
    # clip_envelope_chooser_view_state:
    # audio_input_routing:
    # midi_input_routing
    # audio_output_routing:
    # midi_output_routing:
    mixer: MasterTrackMixer
    # freeze_sequencer: FreezeSequencer
    # device_chain


class EnumEvent(AbletonComponent):  # TimeSignatureEvent
    """
    EnumEvent Class

    Represents an enumeration event in Ableton Live.

    Attributes
    ----------
    id : int
        Unique identifier for the enumeration event.
    time : int
        Time value for the enumeration event.
    value : int
        Value for the enumeration event.

    """

    id: int
    time: int
    value: int


class Automation(AbletonComponent):
    """
    Automation Class

    Represents automation settings in Ableton Live.

    Attributes
    ----------
    events : list[EnumEvent]
        List of enumeration events representing the automation events.
    # automation_transform_view_state: AutomationTransformViewState
        (Commented out) Automation transform view state.


    """

    events: list[EnumEvent]
    # automation_transform_view_state: AutomationTransformViewState


class AutomationEnvelope(AbletonComponent):
    """
    AutomationEnvelope Class

    Represents an automation envelope in Ableton Live.

    Attributes
    ----------
    id : int
        Unique identifier for the automation envelope.
    # envelope_target:
        (Commented out) Envelope target.
    automation : Automation
        Automation settings associated with the envelope.

    """

    id: int
    # envelope_target:
    automation: Automation


class AutomationEnvelopes(AbletonComponent):
    """
    AutomationEnvelopes Class

    Represents a collection of automation envelopes in Ableton Live.

    Attributes
    ----------
    envelopes : list[AutomationEnvelope]
        List of automation envelopes.

    """

    envelopes: list[AutomationEnvelope]


class MasterTrack(AbletonComponent):
    """
    MasterTrack Class

    Represents the master track in Ableton Live.

    Attributes
    ----------
    lom_id : int
        LOM (Live Object Model) identifier for the master track.
    lom_id_view : int
        LOM identifier for the view of the master track.
    is_content_selected_in_document : bool
        Flag indicating whether the master track's content is selected in the document.
    preferred_content_view_mode : int
        Preferred content view mode for the master track.
    track_delay : TrackDelay
        Track delay settings for the master track.
    name : MidiName
        Name settings for the master track.
    color : int
        Color code for the master track.
    automation_envelopes : AutomationEnvelopes
        Collection of automation envelopes associated with the master track.
    track_group_id : int
        Identifier for the track group to which the master track belongs.
    track_unfolded : bool
        Flag indicating whether the master track is unfolded.
    # devices_list_wrapper: lom_id
        (Commented out) Wrapper for the list of devices associated with the master track.
    # clip_slots_list_wrapper
        (Commented out) Wrapper for the list of clip slots associated with the master track.
    view_data : dict
        Dictionary containing view-related data for the master track.
    # take_lanes:
        (Commented out) List of take lanes associated with the master track.
    linked_track_group_id : int
        Identifier for the linked track group.
    device_chain : MasterTrackDeviceChain
        Device chain settings for the master track.

    """

    lom_id: int
    lom_id_view: int
    is_content_selected_in_document: bool
    preferred_content_view_mode: int
    track_delay: TrackDelay
    name: MidiName
    color: int
    automation_envelopes: AutomationEnvelopes
    track_group_id: int
    track_unfolded: bool
    # devices_list_wrapper: lom_id
    # clip_slots_list_wrapper
    view_data: dict
    # take_lanes:
    linked_track_group_id: int
    device_chain: MasterTrackDeviceChain


class PreHearTrack(AbletonComponent):
    """
    PreHearTrack Class

    Represents a pre-hear track in Ableton Live.

    """

    def __init__(self, root: ElementTree.Element):
        return None
