from xml.etree import ElementTree


class MidiTrack:
    id: int
    lom_id: int
    lom_id_view: int
    is_content_selected_in_document: bool
    preferred_content_view_mode: int
    # track_delay: TrackDelay
    # name: Name
    color: int
    # automation_envelopes: List[Envelope]
    track_group: int
    track_unfolded: bool
    devices_list_wrapper: int
    clip_slots_list_wrapper: int
    # view_data: dict
    # take_lanes: List[TakeLane]
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
        self.id = int(root.attrib["Id"])
        self.lom_id = int(root.find("LomId").attrib["Value"])
        self.lom_id_view = int(root.find("LomIdView").attrib["Value"])
        self.is_content_selected_in_document = bool(
            root.find("IsContentSelectedInDocument").attrib["Value"]
        )
        self.preferred_content_view_mode = int(
            root.find("PreferredContentViewMode").attrib["Value"]
        )
        # self.track_delay = int(root.find("TrackDelay"))
        # self.name = int(root.find("Name"))
        self.color = int(root.find("Color").attrib["Value"])
        self.track_group = int(root.find("TrackGroupId").attrib["Value"])
        self.track_unfolded = bool(root.find("TrackUnfolded").attrib["Value"])
        self.devices_list_wrapper = int(root.find("DevicesListWrapper").attrib["LomId"])
        self.clip_slots_list_wrapper = int(root.find("ClipSlotsListWrapper").attrib["LomId"])
        # self.view_data =
        # self.take_lanes =
        self.linked_track_group_id = int(root.find("LinkedTrackGroupId").attrib["Value"])
        self.saved_playing_slot = int(root.find("SavedPlayingSlot").attrib["Value"])
        self.saved_playing_offset = int(root.find("SavedPlayingOffset").attrib["Value"])
        self.freeze = bool(root.find("Freeze").attrib["Value"])
        self.velocity_detail = int(root.find("VelocityDetail").attrib["Value"])
        self.need_arranger_refreeze = bool(root.find("NeedArrangerRefreeze").attrib["Value"])
        self.post_process_freeze_clips = int(root.find("PostProcessFreezeClips").attrib["Value"])
        # self.device_chain = int(root.find("VelocityDetail").attrib["Value"])
        self.re_wire_slave_midi_target_id = int(
            root.find("ReWireSlaveMidiTargetId").attrib["Value"]
        )
        self.pitchbend_range = int(root.find("PitchbendRange").attrib["Value"])
