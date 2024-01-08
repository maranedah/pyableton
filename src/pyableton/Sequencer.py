from .AbletonComponent import AbletonComponent
from .ClipTimeable import ClipTimeable


class FreezeSequencer(AbletonComponent):
    """
    FreezeSequencer Class

    Represents the freeze sequencer in Ableton Live.

    Attributes
    ----------
    lom_id : int
        The Level Of Manipulation (LOM) ID for the freeze sequencer.
    lom_id_view : int
        The view LOM ID for the freeze sequencer.
    is_expanded : bool
        Flag indicating whether the freeze sequencer is expanded.
    modulation_source_count : int
        The count of modulation sources in the freeze sequencer.
    parameters_list_wrapper : int
        Wrapper for parameters list in the freeze sequencer.
    last_selected_timeable_index : int
        Index of the last selected timeable in the freeze sequencer.
    last_selected_clip_envelope_index : int
        Index of the last selected clip envelope in the freeze sequencer.
    is_folded : bool
        Flag indicating whether the freeze sequencer is folded.
    should_show_preset_name : bool
        Flag indicating whether the preset name should be shown in the freeze sequencer.
    user_name : str
        The user-assigned name for the freeze sequencer.
    annotation : str
        Annotation information for the freeze sequencer.
    monitoring_enum : int
        Enumeration representing the monitoring state in the freeze sequencer.
    pitch_view_scroll_position : int
        Scroll position for pitch view in the freeze sequencer.
    sample_offset_modulation_scroll_position : int
        Scroll position for sample offset modulation in the freeze sequencer.

    """

    lom_id: int
    lom_id_view: int
    is_expanded: bool
    # on: On
    modulation_source_count: int
    parameters_list_wrapper: int
    # pointee: int
    last_selected_timeable_index: int
    last_selected_clip_envelope_index: int
    # last_preset_ref: LastPresetRef
    # locked_scripts: LockedScripts
    is_folded: bool
    should_show_preset_name: bool
    user_name: str
    annotation: str
    # source_context: SourceContext
    # clip_slot_list: List[ClipSlot]
    monitoring_enum: int
    # sample: Sample
    # volume_modulation_target: VolumeModulationTarget
    # transposition_modulation_target: Transposition_ModulationTarget
    # grain_size_modulation_target: GrainSizeModulationTarget
    # flux_modulation_target: FluxModulationTarget
    # sample_offset_modulation_target: SampleOffsetModulationTarget
    pitch_view_scroll_position: int
    sample_offset_modulation_scroll_position: int
    # recorder: Recorder


class AutomationTarget(AbletonComponent):
    """
    AutomationTarget Class

    Represents the automation target in Ableton Live.

    Attributes
    ----------
    id : int
        The unique identifier for the automation target.
    lock_envelope : int
        Lock envelope setting for the automation target.

    """

    id: int
    lock_envelope: int


class MidiCCOnOffThresholds(AbletonComponent):
    """
    MidiCCOnOffThresholds Class

    Represents MIDI Continuous Controller (CC) on/off thresholds.

    Attributes
    ----------
    min : int
        Minimum threshold value.
    max : int
        Maximum threshold value.

    """

    min: int
    max: int


class On(AbletonComponent):
    """
    On Class

    Represents the 'On' state in Ableton Live.

    Attributes
    ----------
    lom_id : int
        The Level Of Manipulation (LOM) ID for the 'On' state.
    manual : bool
        Flag indicating whether the state is set manually.
    automation_target : AutomationTarget
        Automation target settings for the 'On' state.
    midi_CC_on_off_thresholds : MidiCCOnOffThresholds
        MIDI CC on/off thresholds for the 'On' state.

    """

    lom_id: int
    manual: bool
    automation_target: AutomationTarget
    midi_CC_on_off_thresholds: MidiCCOnOffThresholds


class MainSequencer(AbletonComponent):
    """
    MainSequencer Class

    Represents the main sequencer in Ableton Live.

    Attributes
    ----------
    lom_id : int
        The Level Of Manipulation (LOM) ID for the main sequencer.
    lom_id_view : int
        The view LOM ID for the main sequencer.
    is_expanded : bool
        Flag indicating whether the main sequencer is expanded.
    on : On
        'On' state settings for the main sequencer.
    modulation_source_count : int
        The count of modulation sources in the main sequencer.
    parameters_list_wrapper : int
        Wrapper for parameters list in the main sequencer.
    pointee : int
        The pointee setting for the main sequencer.
    last_selected_timeable_index : int
        Index of the last selected timeable in the main sequencer.
    last_selected_clip_envelope_index : int
        Index of the last selected clip envelope in the main sequencer.
    is_folded : bool
        Flag indicating whether the main sequencer is folded.
    should_show_preset_name : bool
        Flag indicating whether the preset name should be shown in the main sequencer.
    user_name : str
        The user-assigned name for the main sequencer.
    annotation : str
        Annotation information for the main sequencer.
    monitoring_enum : int
        Enumeration representing the monitoring state in the main sequencer.
    clip_timeable : ClipTimeable
        Clip timeable settings for the main sequencer.

    """

    lom_id: int
    lom_id_view: int
    is_expanded: bool
    on: On
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
    # clip_slot_list: List[ClipSlot]
    monitoring_enum: int
    clip_timeable: ClipTimeable
    # recorder: Recorder
    # midi_controllers: List[MidiController]
