from xml.etree import ElementTree

from .AbletonComponent import AbletonComponent
from .Midi import DeviceChain, MidiName

# from .DeviceChain import DeviceChain
# from .Name import Name
# from .TrackDelay import TrackDelay


class Track(AbletonComponent):
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

    def __init__(self, root):
        super().__init__(root)


class TrackDelay(AbletonComponent):
    value: int
    is_value_sample_based: bool

    def __init__(self, root: ElementTree.Element):
        super().__init__(root)


class MidiTrack(Track):
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

    def __init__(self, root: ElementTree.Element):
        super().__init__(root)


class ReturnTrack(Track):
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
    def __init__(self, root: ElementTree.Element):
        return None


class VisibleTracksListWrapper(AbletonComponent):
    def __init__(self, root: ElementTree.Element):
        return None


class Tempo(AbletonComponent):
    lom_id: int
    manual: int
    # midi_controller_range
    # automation_target
    # modulation_target


class MasterTrackMixer(AbletonComponent):
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
    id: int
    time: int
    value: int


class Automation(AbletonComponent):
    events: list[EnumEvent]
    # automation_transform_view_state: AutomationTransformViewState


class AutomationEnvelope(AbletonComponent):
    id: int
    # envelope_target:
    automation: Automation


class AutomationEnvelopes(AbletonComponent):
    envelopes: list[AutomationEnvelope]


class MasterTrack(AbletonComponent):
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
    def __init__(self, root: ElementTree.Element):
        return None


class ReturnTracksListWrapper(AbletonComponent):
    def __init__(self, root: ElementTree.Element):
        return None
