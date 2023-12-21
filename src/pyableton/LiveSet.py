from .AbletonComponent import AbletonComponent
from .DetailClipKeyMidi import DetailClipKeyMidi
from .Grid import Grid
from .LinkedTrackGroups import LinkedTrackGroups
from .Locator import Locator
from .Scene import Scene, ScenesListWrapper
from .SequencerNavigator import SequencerNavigator
from .SignalModulations import SignalModulations
from .Track import (
    MasterTrack,
    PreHearTrack,
    ReturnTracksListWrapper,
    Track,
    TracksListWrapper,
    VisibleTracksListWrapper,
)
from .Transport import Transport
from .VideoWindowRect import VideoWindowRect
from .ViewStates import ViewStates


class AutoColorPickerForPlayerAndGroupTracks(AbletonComponent):
    next_color_index: int


class AutoColorPickerForReturnAndMasterTracks(AbletonComponent):
    next_color_index: int


class ExpressionLane(AbletonComponent):
    id: int
    type: int
    size: int
    is_minimized: bool


class GroovePool(AbletonComponent):
    lom_id: int
    # Grooves: list[None]


class ScaleInformation(AbletonComponent):
    root_note: int
    name: str


class SendPreBool(AbletonComponent):
    id: int
    value: bool


class SessionScrollerPos(AbletonComponent):
    x: int
    y: int


class SongMasterValues(AbletonComponent):
    session_scroller_pos: SessionScrollerPos


class TimeSelection(AbletonComponent):
    anchor_time: int
    other_time: int


class LiveSet(AbletonComponent):
    next_pointee_id: int
    overwrite_protection_number: int
    lom_id: int
    lom_id_view: int
    tracks: list[Track]
    master_track: MasterTrack
    pre_hear_track: PreHearTrack
    sends_pre: list[SendPreBool]
    scenes: list[Scene]
    transport: Transport
    song_master_values: SongMasterValues
    signal_modulations: SignalModulations
    global_quantisation: int
    auto_quantisation: int
    grid: Grid
    scale_information: ScaleInformation
    in_key: bool
    smpte_format: int
    time_selection: TimeSelection
    sequencer_navigator: SequencerNavigator
    is_content_splitter_open: bool
    is_expression_splitter_open: bool
    expression_lanes: list[ExpressionLane]
    content_lanes: list[ExpressionLane]
    view_state_fx_slot_count: int
    view_state_session_mixer_height: int
    locators: list[Locator]
    detail_clip_key_midis: list[DetailClipKeyMidi]
    tracks_list_wrapper: TracksListWrapper
    visible_tracks_list_wrapper: VisibleTracksListWrapper
    return_tracks_list_wrapper: ReturnTracksListWrapper
    scenes_list_wrapper: ScenesListWrapper
    cue_points_list_wrapper: int
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
