from xml.etree import ElementTree

from ..AbletonComponent import AbletonComponent

# from .DeviceChain import DeviceChain
from .Name import Name
from .TrackDelay import TrackDelay


class MidiTrack(AbletonComponent):
    id: int
    lom_id: int
    lom_id_view: int
    is_content_selected_in_document: bool
    preferred_content_view_mode: int
    track_delay: TrackDelay
    name: Name
    color: int
    # automation_envelopes: List[Envelope]
    track_group_id: int
    track_unfolded: bool
    devices_list_wrapper: int
    clip_slots_list_wrapper: int
    # view_data: dict
    # take_lanes: list[TakeLane]
    linked_track_group_id: int
    saved_playing_slot: int
    saved_playing_offset: int
    freeze: bool
    velocity_detail: int
    need_arranger_refreeze: bool
    post_process_freeze_clips: int
    # device_chain: DeviceChain
    re_wire_slave_midi_target_id: int
    pitchbend_range: int

    def __init__(self, root: ElementTree.Element):
        super().__init__(root)
