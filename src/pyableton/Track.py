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


class MasterTrack(AbletonComponent):
    def __init__(self, root: ElementTree.Element):
        return None


class PreHearTrack(AbletonComponent):
    def __init__(self, root: ElementTree.Element):
        return None


class ReturnTracksListWrapper(AbletonComponent):
    def __init__(self, root: ElementTree.Element):
        return None
