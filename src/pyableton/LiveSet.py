from .AbletonComponent import AbletonComponent
from .Grid import Grid
from .Scene import Scene, ScenesListWrapper
from .Track import (
    MasterTrack,
    PreHearTrack,
    Track,
    TracksListWrapper,
    VisibleTracksListWrapper,
)


class AutoColorPickerForPlayerAndGroupTracks(AbletonComponent):
    """
    AutoColorPickerForPlayerAndGroupTracks Class

    Represents an Auto Color Picker for player and group tracks.

    Attributes
    ----------
    next_color_index : int
        The index for the next color.

    """

    next_color_index: int


class AutoColorPickerForReturnAndMasterTracks(AbletonComponent):
    """
    AutoColorPickerForReturnAndMasterTracks Class

    Represents an Auto Color Picker for return and master tracks.

    Attributes
    ----------
    next_color_index : int
        The index for the next color.

    """

    next_color_index: int


class ExpressionLane(AbletonComponent):
    """
    ExpressionLane Class

    Represents an expression lane.

    Attributes
    ----------
    id : int
        The ID of the expression lane.
    type : int
        The type of the expression lane.
    size : int
        The size of the expression lane.
    is_minimized : bool
        Flag indicating if the expression lane is minimized.

    """

    id: int
    type: int
    size: int
    is_minimized: bool


class GroovePool(AbletonComponent):
    """
    GroovePool Class

    Represents a Groove Pool.

    Attributes
    ----------
    lom_id : int
        The Level of Mess (LOM) ID.
    Grooves : list[None]
        List of grooves (currently set as None).

    """

    lom_id: int
    # Grooves: list[None]


class Locator:
    """
    Locator Class

    Represents a locator.

    Note
    ----
    This class has a placeholder implementation.

    """

    def __init__(self, root):
        return None


class DetailClipKeyMidi:
    """
    DetailClipKeyMidi Class

    Represents details about the clip's key MIDI.

    Note
    ----
    This class has a placeholder implementation.

    """

    def __init__(self, root):
        return None


class LinkedTrackGroups:
    """
    LinkedTrackGroups Class

    Represents linked track groups.

    Note
    ----
    This class has a placeholder implementation.

    """

    def __init__(self, root):
        return None


class ScaleInformation(AbletonComponent):
    """
    ScaleInformation Class

    Represents information about the scale.

    Attributes
    ----------
    root_note : int
        The root note of the scale.
    name : str
        The name of the scale.

    """

    root_note: int
    name: str


class SendPreBool(AbletonComponent):
    """
    SendPreBool Class

    Represents a send with a boolean value.

    Attributes
    ----------
    id : int
        The ID of the send.
    value : bool
        The boolean value of the send.

    """

    id: int
    value: bool


class BeatTimeHelper(AbletonComponent):
    """
    BeatTimeHelper Class

    Represents a helper for beat time.

    Attributes
    ----------
    current_zoom : float
        The current zoom level.

    """

    current_zoom: float


class ScrollerPos(AbletonComponent):
    """
    ScrollerPos Class

    Represents the position of a scroller.

    Attributes
    ----------
    x : int
        The X-coordinate of the scroller position.
    y : int
        The Y-coordinate of the scroller position.

    """

    x: int
    y: int


class ClientSize(AbletonComponent):
    """
    ClientSize Class

    Represents the size of a client.

    Attributes
    ----------
    x : int
        The width of the client.
    y : int
        The height of the client.

    """

    x: int
    y: int


class SequencerNavigator(AbletonComponent):
    """
    SequencerNavigator Class

    Represents a sequencer navigator.

    Attributes
    ----------
    beat_time_helper : BeatTimeHelper
        The beat time helper.
    scroller_pos : ScrollerPos
        The scroller position.
    client_size : ClientSize
        The client size.

    """

    beat_time_helper: BeatTimeHelper
    scroller_pos: ScrollerPos
    client_size: ClientSize


class SessionScrollerPos(AbletonComponent):
    """
    SessionScrollerPos Class

    Represents the position of a scroller in a session.

    Attributes
    ----------
    x : int
        The X-coordinate of the scroller position.
    y : int
        The Y-coordinate of the scroller position.

    """

    x: int
    y: int


class SignalModulations(AbletonComponent):
    """
    SignalModulations Class

    Represents signal modulations.

    Note
    ----
    This class has a placeholder implementation.

    """

    def __init__(self, root):
        return None


class SongMasterValues(AbletonComponent):
    """
    SongMasterValues Class

    Represents master values for a song.

    Attributes
    ----------
    session_scroller_pos : SessionScrollerPos
        The session scroller position.

    """

    session_scroller_pos: SessionScrollerPos


class TimeSelection(AbletonComponent):
    """
    TimeSelection Class

    Represents the time selection.

    Attributes
    ----------
    anchor_time : int
        The anchor time of the selection.
    other_time : int
        The other time of the selection.

    """

    anchor_time: int
    other_time: int


class Transport(AbletonComponent):
    """
    Transport Class

    Represents the transport controls.

    Attributes
    ----------
    phase_nudge_tempo : int
        The phase nudge tempo.
    loop_on : bool
        Flag indicating if looping is enabled.
    loop_start : int
        The start time of the loop.
    loop_length : int
        The length of the loop.
    loop_is_song_start : bool
        Flag indicating if the loop starts at the beginning of the song.
    current_time : int
        The current time position.
    punch_in : bool
        Flag indicating if punch-in is enabled.
    punch_out : bool
        Flag indicating if punch-out is enabled.
    metronome_tick_duration : int
        The duration of the metronome tick.
    draw_mode : bool
        Flag indicating if draw mode is enabled.

    """

    phase_nudge_tempo: int
    loop_on: bool
    loop_start: int
    loop_length: int
    loop_is_song_start: bool
    current_time: float
    punch_in: bool
    punch_out: bool
    metronome_tick_duration: int
    draw_mode: bool


class VideoWindowRect(AbletonComponent):
    """
    VideoWindowRect Class

    Represents the rectangle of a video window.

    Attributes
    ----------
    top : int
        The top coordinate of the rectangle.
    left : int
        The left coordinate of the rectangle.
    bottom : int
        The bottom coordinate of the rectangle.
    right : int
        The right coordinate of the rectangle.

    """

    top: int
    left: int
    bottom: int
    right: int


class ViewStates(AbletonComponent):
    """
    ViewStates Class

    Represents view states.

    Attributes
    ----------
    session_IO : int
        Session I/O view state.
    session_sends : int
        Session sends view state.
    session_returns : int
        Session returns view state.
    session_mixer : int
        Session mixer view state.
    session_track_delay : int
        Session track delay view state.
    session_cross_fade : int
        Session cross-fade view state.
    session_show_over_view : int
        Session show overview view state.
    arranger_IO : int
        Arranger I/O view state.
    arranger_returns : int
        Arranger returns view state.
    arranger_mixer : int
        Arranger mixer view state.
    arranger_track_delay : int
        Arranger track delay view state.
    arranger_show_over_view : int
        Arranger show overview view state.

    """

    session_IO: int
    session_sends: int
    session_returns: int
    session_mixer: int
    session_track_delay: int
    session_cross_fade: int
    session_show_over_view: int
    arranger_IO: int
    arranger_returns: int
    arranger_mixer: int
    arranger_track_delay: int
    arranger_show_over_view: int


class LiveSet(AbletonComponent):
    """
    LiveSet Class

    Represents an Ableton Live set.

    Attributes
    ----------
    next_pointee_id : int
        The next pointee identifier in the Ableton Live set.
    overwrite_protection_number : int
        The overwrite protection number for the Ableton Live set.
    lom_id : int
        The Level of Mess (LOM) ID associated with the Ableton Live set.
    lom_id_view : int
        The LOM ID view of the Ableton Live set.
    tracks : list[Track]
        List of tracks in the Ableton Live set.
    master_track : MasterTrack
        The master track in the Ableton Live set.
    pre_hear_track : PreHearTrack
        The pre-hear track in the Ableton Live set.
    sends_pre : list[SendPreBool]
        List of pre-send boolean values in the Ableton Live set.
    scenes : list[Scene]
        List of scenes in the Ableton Live set.
    transport : Transport
        The transport settings in the Ableton Live set.
    song_master_values : SongMasterValues
        The song master values in the Ableton Live set.
    signal_modulations : SignalModulations
        The signal modulations in the Ableton Live set.
    global_quantisation : int
        The global quantization setting in the Ableton Live set.
    auto_quantisation : int
        The auto quantization setting in the Ableton Live set.
    grid : Grid
        The grid settings in the Ableton Live set.
    scale_information : ScaleInformation
        The scale information in the Ableton Live set.
    in_key : bool
        Flag indicating whether the Ableton Live set is in key.
    smpte_format : int
        The SMPTE format setting in the Ableton Live set.
    time_selection : TimeSelection
        The time selection settings in the Ableton Live set.
    sequencer_navigator : SequencerNavigator
        The sequencer navigator settings in the Ableton Live set.
    is_content_splitter_open : bool
        Flag indicating whether the content splitter is open in the Ableton Live set.
    is_expression_splitter_open : bool
        Flag indicating whether the expression splitter is open in the Ableton Live set.
    expression_lanes : list[ExpressionLane]
        List of expression lanes in the Ableton Live set.
    content_lanes : list[ExpressionLane]
        List of content lanes in the Ableton Live set.
    view_state_fx_slot_count : int
        The view state FX slot count in the Ableton Live set.
    view_state_session_mixer_height : int
        The view state session mixer height in the Ableton Live set.
    locators : list[Locator]
        List of locators in the Ableton Live set.
    detail_clip_key_midis : list[DetailClipKeyMidi]
        List of detail clip key MIDI events in the Ableton Live set.
    tracks_list_wrapper : TracksListWrapper
        The tracks list wrapper in the Ableton Live set.
    visible_tracks_list_wrapper : VisibleTracksListWrapper
        The visible tracks list wrapper in the Ableton Live set.
    return_tracks_list_wrapper : int
        The return tracks list wrapper in the Ableton Live set.
    scenes_list_wrapper : ScenesListWrapper
        The scenes list wrapper in the Ableton Live set.
    cue_points_list_wrapper : int
        The cue points list wrapper in the Ableton Live set.
    chooser_bar : int
        The chooser bar setting in the Ableton Live set.
    annotation : str
        The annotation of the Ableton Live set.
    solo_or_pfl_saved_value : bool
        Flag indicating the solo or pre-fader listen saved value in the Ableton Live set.
    solo_in_place : bool
        Flag indicating whether solo in place is enabled in the Ableton Live set.
    crossfade_curve : int
        The crossfade curve setting in the Ableton Live set.
    latency_compensation : int
        The latency compensation setting in the Ableton Live set.
    highlighted_track_index : int
        The index of the highlighted track in the Ableton Live set.
    groove_pool : GroovePool
        The groove pool settings in the Ableton Live set.
    automation_mode : bool
        Flag indicating whether automation mode is enabled in the Ableton Live set.
    snap_automation_to_grid : bool
        Flag indicating whether to snap automation to the grid in the Ableton Live set.
    arrangement_overdub : bool
        Flag indicating whether arrangement overdub is enabled in the Ableton Live set.
    color_sequence_index : int
        The color sequence index in the Ableton Live set.
    auto_color_picker_for_player_and_group_tracks : AutoColorPickerForPlayerAndGroupTracks
        The auto color picker settings for player and group tracks in the Ableton Live set.
    auto_color_picker_for_return_and_master_tracks : AutoColorPickerForReturnAndMasterTracks
        The auto color picker settings for return and master tracks in the Ableton Live set.
    view_data : dict
        The view data in the Ableton Live set.
    reset_nonautomated_midi_controllers_on_clip_starts : bool
        Flag indicating whether to reset non-automated MIDI controllers on clip starts
        in the Ableton Live set.
    midi_fold_in : bool
        Flag indicating whether MIDI fold-in is enabled in the Ableton Live set.
    midi_fold_mode : bool
        Flag indicating the MIDI fold mode setting in the Ableton Live set.
    multi_clip_focus_mode : bool
        Flag indicating the multi-clip focus mode setting in the Ableton Live set.
    multi_clip_loop_bar_height : int
        The multi-clip loop bar height setting in the Ableton Live set.
    midi_prelisten : bool
        Flag indicating whether MIDI prelisten is enabled in the Ableton Live set.
    linked_track_groups : LinkedTrackGroups
        The linked track groups settings in the Ableton Live set.
    accidental_spelling_preference : int
        The accidental spelling preference setting in the Ableton Live set.
    prefer_flat_root_note : bool
        Flag indicating whether a flat root note is preferred in the Ableton Live set.
    use_warper_legacy_hi_q_mode : bool
        Flag indicating whether to use the warper legacy high Q mode in the Ableton Live set.
    video_window_rect : VideoWindowRect
        The video window rectangle settings in the Ableton Live set.
    show_video_window : bool
        Flag indicating whether to show the video window in the Ableton Live set.
    track_header_width : int
        The track header width setting in the Ableton Live set.
    view_state_arranger_has_detail : bool
        Flag indicating whether the arranger has detail in the Ableton Live set.
    view_state_session_has_detail : bool
        Flag indicating whether the session view has detail in the Ableton Live set.
    view_state_detail_is_sample : bool
        Flag indicating whether the detail is a sample in the Ableton Live set.
    view_states : ViewStates
        The view states settings in the Ableton Live set.

    """

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
    return_tracks_list_wrapper: int
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
