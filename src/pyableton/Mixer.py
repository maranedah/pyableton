from .AbletonComponent import AbletonComponent


class Pan(AbletonComponent):
    """
    Pan Class

    Represents pan information in Ableton Live.

    Attributes
    ----------
    lom_id : int
        The Level Of Manipulation (LOM) ID for pan.
    manual : int
        The manual pan value.

    """

    lom_id: int
    manual: int
    # midi_controller_range: MidiControllerRange
    # automation_target: AutomationTarget
    # modulation_target: ModulationTarget


class Mixer(AbletonComponent):
    """
    Mixer Class

    Represents mixer information in Ableton Live.

    Attributes
    ----------
    lom_id : int
        The Level Of Manipulation (LOM) ID for the mixer.
    lom_id_view : int
        The LOM ID for the mixer view.
    is_expanded : bool
        Flag indicating whether the mixer is expanded.
    modulation_source_count : int
        The count of modulation sources in the mixer.
    parameters_list_wrapper : int
        Wrapper for parameters list in the mixer.
    pointee : int
        The pointee ID for the mixer.
    last_selected_timeable_index : int
        Index of the last selected timeable.
    last_selected_clip_envelope_index : int
        Index of the last selected clip envelope.
    is_folded : bool
        Flag indicating whether the mixer is folded.
    should_show_preset_name : bool
        Flag indicating whether the preset name should be shown.
    user_name : str
        User-defined name for the mixer.
    annotation : str
        Annotation information for the mixer.
    solo_sink : bool
        Flag indicating whether solo sink is enabled.
    pan_mode : int
        The pan mode for the mixer.
    pan : Pan
        Pan information for the mixer.
    split_stereo_pan_l : Pan
        Pan information for the left channel in split stereo mode.
    split_stereo_pan_r : Pan
        Pan information for the right channel in split stereo mode.
    view_state_sesstion_track_width : int
        Width of the session track in the view state.
    cross_fade_state: CrossFadeState
    sends_list_wrapper : int
        Wrapper for sends list in the mixer.

    """

    lom_id: int
    lom_id_view: int
    is_expanded: bool
    # on: On
    modulation_source_count: int
    parameters_list_wrapper: int
    pointee: int
    last_selected_timeable_index: int
    last_selected_clip_envelope_index: int
    # last_preset_ref: LastPresetRef
    # locked_scripts: LockedScripts
    is_folded: bool
    should_show_preset_name: bool
    user_name: str
    annotation: str
    # source_context: SourceContext
    # sends: List[TrackSendHolder]
    # speaker: Speaker
    solo_sink: bool
    pan_mode: int
    pan: Pan
    split_stereo_pan_l: Pan
    split_stereo_pan_r: Pan
    # volume: Volume
    view_state_sesstion_track_width: int
    # cross_fade_state: CrossFadeState
    sends_list_wrapper: int
