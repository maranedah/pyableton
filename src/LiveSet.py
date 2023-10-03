from typing import List
from xml.etree import ElementTree

from MidiTrack import MidiTrack
from MasterTrack import MasterTrack
from PreHearTrack import PreHearTrack
from SendsPre import SendsPre
from Scene import Scene
from Transport import Transport
from SongMasterValues import SongMasterValues
from SignalModulations import SignalModulations
from GlobalQuantisation import GlobalQuantisation
from AutoQuantisation import AutoQuantisation
from Grid import Grid
from ScaleInformation import ScaleInformation
from TimeSelection import TimeSelection
from SequencerNavigator import SequencerNavigator
from ExpressionLane import ExpressionLane
from ContentLane import ContentLane
from Locator import Locator
from DetailClipKeyMidi import DetailClipKeyMidi
from TracksListWrapper import TracksListWrapper
from VisibleTracksListWrapper import VisibleTracksListWrapper
from ReturnTracksListWrapper import ReturnTracksListWrapper
from ScenesListWrapper import ScenesListWrapper
from CuePointsListWrapper import CuePointsListWrapper
from GroovePool import GroovePool
from AutoColorPickerForPlayerAndGroupTracks import AutoColorPickerForPlayerAndGroupTracks
from AutoColorPickerForReturnAndMasterTracks import AutoColorPickerForReturnAndMasterTracks
from LinkedTrackGroups import LinkedTrackGroups
from VideoWindowRect import VideoWindowRect
from ViewStates import ViewStates


class LiveSet:
    next_pointee_id: int
    overwrite_protection_number: int
    lom_id: int
    lom_id_view: int
    tracks: List[MidiTrack]
    master_track: MasterTrack
    pre_hear_track: PreHearTrack
    sends_pre: SendsPre
    scenes: List[Scene]
    transport: Transport
    song_master_values: SongMasterValues
    signal_modulations: SignalModulations
    global_quantisation: GlobalQuantisation
    auto_quantisation: AutoQuantisation
    grid: Grid
    scale_information: ScaleInformation
    in_key: bool
    smpte_format: int
    time_selection: TimeSelection
    sequencer_navigator: SequencerNavigator
    is_content_splitter_open: bool
    is_expression_splitter_open: bool
    expression_lanes: List[ExpressionLane]
    content_lanes: List[ContentLane]
    view_state_fx_slot_count: int
    view_state_session_mixer_height: int
    locators: List[Locator]
    detail_clipkey_midis: List[DetailClipKeyMidi]
    tracks_list_wrapper: TracksListWrapper
    visible_tracks_list_wrapper: VisibleTracksListWrapper
    return_tracks_list_wrapper: ReturnTracksListWrapper
    scenes_list_wrapper: ScenesListWrapper
    cue_points_list_wrapper: CuePointsListWrapper
    chooser_bar: int
    annotation: str
    solo_or_pfl_saved_value: bool
    solo_in_place: bool
    crossfade_curve: int
    latency_compensation: int
    highlighted_track_index: int
    groove_pool: GroovePool
    automation_mode: bool
    snap_automation_to_grid: bool
    arrangement_overdub: bool
    color_sequence_index: int
    auto_color_picker_for_player_and_group_tracks: AutoColorPickerForPlayerAndGroupTracks
    auto_color_picker_for_return_and_master_tracks: AutoColorPickerForReturnAndMasterTracks
    view_data: dict
    reset_nonautomated_midi_controllers_on_clip_starts: bool
    midi_fold_in: bool
    midi_fold_mode: bool
    multi_clip_focus_mode: bool
    multi_clip_loop_bar_height: int
    midi_prelisten: bool
    linked_track_groups: LinkedTrackGroups
    accidental_spelling_preference: int
    prefer_flat_root_note: bool
    use_warper_legacy_hi_q_mode: bool
    video_window_rect: VideoWindowRect
    show_video_window: bool
    track_header_width: int
    view_state_arranger_has_detail: bool
    view_state_session_has_detail: bool
    view_state_detail_is_sample: bool
    view_states: ViewStates

    def __init__(
        self, 
        root: ElementTree.Element
    ):
        breakpoint()
        self.next_pointee_id = int(root.find("NextPointeeId").attrib["Value"])
        self.overwrite_protection_number = int(root.find("OverwriteProtectionNumber").attrib["Value"])
        self.lom_id = int(root.find("LomId").attrib["Value"])
        self.lom_id_view = int(root.find("LomIdView").attrib["Value"]) 
        """
        self.tracks: List[MidiTrack]
        self.master_track: MasterTrack
        self.pre_hear_track: PreHearTrack
        self.sends_pre: SendsPre
        self.scenes: List[Scene]
        self.transport: Transport
        self.song_master_values: SongMasterValues
        self.signal_modulations: SignalModulations
        self.global_quantisation: GlobalQuantisation
        self.auto_quantisation: AutoQuantisation
        self.grid: Grid
        self.scale_information: ScaleInformation
        self.in_key: bool
        self.smpte_format: int
        self.time_selection: TimeSelection
        self.sequencer_navigator: SequencerNavigator
        self.is_content_splitter_open: bool
        self.is_expression_splitter_open: bool
        self.expression_lanes: List[ExpressionLane]
        self.content_lanes: List[ContentLane]
        self.view_state_fx_slot_count: int
        self.view_state_session_mixer_height: int
        self.locators: List[Locator]
        self.detail_clipkey_midis: List[DetailClipKeyMidi]
        self.tracks_list_wrapper: TracksListWrapper
        self.visible_tracks_list_wrapper: VisibleTracksListWrapper
        self.return_tracks_list_wrapper: ReturnTracksListWrapper
        self.scenes_list_wrapper: ScenesListWrapper
        self.cue_points_list_wrapper: CuePointsListWrapper
        self.chooser_bar: int
        self.annotation: str
        self.solo_or_pfl_saved_value: bool
        self.solo_in_place: bool
        self.crossfade_curve: int
        self.latency_compensation: int
        self.highlighted_track_index: int
        self.groove_pool: GroovePool
        self.automation_mode: bool
        self.snap_automation_to_grid: bool
        self.arrangement_overdub: bool
        self.color_sequence_index: int
        self.auto_color_picker_for_player_and_group_tracks: AutoColorPickerForPlayerAndGroupTracks
        self.auto_color_picker_for_return_and_master_tracks: AutoColorPickerForReturnAndMasterTracks
        self.view_data: dict
        self.reset_nonautomated_midi_controllers_on_clip_starts: bool
        self.midi_fold_in: bool
        self.midi_fold_mode: bool
        self.multi_clip_focus_mode: bool
        self.multi_clip_loop_bar_height: int
        self.midi_prelisten: bool
        self.linked_track_groups: LinkedTrackGroups
        self.accidental_spelling_preference: int
        self.prefer_flat_root_note: bool
        self.use_warper_legacy_hi_q_mode: bool
        self.video_window_rect: VideoWindowRect
        self.show_video_window: bool
        self.track_header_width: int
        self.view_state_arranger_has_detail: bool
        self.view_state_session_has_detail: bool
        self.view_state_detail_is_sample: bool
        self.view_states: ViewStates
        """