from typing import List
from xml.etree import ElementTree

from .AutoColorPickerForPlayerAndGroupTracks import (
    AutoColorPickerForPlayerAndGroupTracks,
)
from .AutoColorPickerForReturnAndMasterTracks import (
    AutoColorPickerForReturnAndMasterTracks,
)
from .AutoQuantisation import AutoQuantisation
from .ContentLane import ContentLane
from .CuePointsListWrapper import CuePointsListWrapper
from .DetailClipKeyMidi import DetailClipKeyMidi
from .ExpressionLane import ExpressionLane
from .GlobalQuantisation import GlobalQuantisation
from .Grid import Grid
from .GroovePool import GroovePool
from .LinkedTrackGroups import LinkedTrackGroups
from .Locator import Locator
from .MasterTrack import MasterTrack
from .MidiTrack import MidiTrack
from .PreHearTrack import PreHearTrack
from .ReturnTracksListWrapper import ReturnTracksListWrapper
from .ScaleInformation import ScaleInformation
from .Scene import Scene
from .ScenesListWrapper import ScenesListWrapper
from .SendsPre import SendsPre
from .SequencerNavigator import SequencerNavigator
from .SignalModulations import SignalModulations
from .SongMasterValues import SongMasterValues
from .TimeSelection import TimeSelection
from .TracksListWrapper import TracksListWrapper
from .Transport import Transport
from .VideoWindowRect import VideoWindowRect
from .ViewStates import ViewStates
from .VisibleTracksListWrapper import VisibleTracksListWrapper


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

    def __init__(self, root: ElementTree.Element):
        self.next_pointee_id = int(root.find("NextPointeeId").attrib["Value"])
        self.overwrite_protection_number = int(
            root.find("OverwriteProtectionNumber").attrib["Value"]
        )
        self.lom_id = int(root.find("LomId").attrib["Value"])
        self.lom_id_view = int(root.find("LomIdView").attrib["Value"])
        self.tracks = [
            MidiTrack(x) for x in root.find("Tracks").findall("./") if x.tag == "MidiTrack"
        ]
        """
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
        """
        self.in_key = bool(root.find("InKey").attrib["Value"])
        self.smpte_format = int(root.find("SmpteFormat").attrib["Value"])
        """
        self.time_selection: TimeSelection
        self.sequencer_navigator: SequencerNavigator
        """
        self.is_content_splitter_open = bool(root.find("IsContentSplitterOpen").attrib["Value"])
        self.is_expression_splitter_open = bool(
            root.find("IsExpressionSplitterOpen").attrib["Value"]
        )
        """
        self.expression_lanes: List[ExpressionLane]
        self.content_lanes: List[ContentLane]
        """
        self.view_state_fx_slot_count = int(root.find("ViewStateFxSlotCount").attrib["Value"])
        self.view_state_session_mixer_height = int(
            root.find("ViewStateSessionMixerHeight").attrib["Value"]
        )
        """
        self.locators: List[Locator]
        self.detail_clipkey_midis: List[DetailClipKeyMidi]
        self.tracks_list_wrapper: TracksListWrapper
        self.visible_tracks_list_wrapper: VisibleTracksListWrapper
        self.return_tracks_list_wrapper: ReturnTracksListWrapper
        self.scenes_list_wrapper: ScenesListWrapper
        self.cue_points_list_wrapper: CuePointsListWrapper
        """
        self.chooser_bar = int(root.find("ChooserBar").attrib["Value"])
        self.annotation = root.find("Annotation").attrib["Value"]
        self.solo_or_pfl_saved_value = bool(root.find("SoloOrPflSavedValue").attrib["Value"])
        self.solo_in_place = bool(root.find("SoloInPlace").attrib["Value"])
        self.crossfade_curve = int(root.find("CrossfadeCurve").attrib["Value"])
        self.latency_compensation = int(root.find("LatencyCompensation").attrib["Value"])
        self.highlighted_track_index = int(root.find("HighlightedTrackIndex").attrib["Value"])
        """
        self.groove_pool: GroovePool
        """
        self.automation_mode = bool(root.find("AutomationMode").attrib["Value"])
        self.snap_automation_to_grid = bool(root.find("SnapAutomationToGrid").attrib["Value"])
        self.arrangement_overdub = bool(root.find("ArrangementOverdub").attrib["Value"])
        self.color_sequence_index = int(root.find("ColorSequenceIndex").attrib["Value"])
        """
        self.auto_color_picker_for_player_and_group_tracks: AutoColorPickerForPlayerAndGroupTracks
        self.auto_color_picker_for_return_and_master_tracks: AutoColorPickerForReturnAndMasterTracks
        self.view_data: dict
        """
        self.reset_nonautomated_midi_controllers_on_clip_starts = bool(
            root.find("ResetNonautomatedMidiControllersOnClipStarts").attrib["Value"]
        )
        self.midi_fold_in = bool(root.find("MidiFoldIn").attrib["Value"])
        self.midi_fold_mode = bool(root.find("MidiFoldMode").attrib["Value"])
        self.multi_clip_focus_mode = bool(root.find("MultiClipFocusMode").attrib["Value"])
        self.multi_clip_loop_bar_height = int(root.find("MultiClipLoopBarHeight").attrib["Value"])
        self.midi_prelisten = bool(root.find("MidiPrelisten").attrib["Value"])
        """
        self.linked_track_groups: LinkedTrackGroups
        """
        self.accidental_spelling_preference: int
        self.prefer_flat_root_note: bool
        self.use_warper_legacy_hi_q_mode: bool
        """
        self.video_window_rect: VideoWindowRect
        """
        self.show_video_window: bool
        self.track_header_width: int
        self.view_state_arranger_has_detail: bool
        self.view_state_session_has_detail: bool
        self.view_state_detail_is_sample: bool
        self.view_states: ViewStates(root.find("ViewStates"))
