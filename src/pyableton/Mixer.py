from xml.etree import ElementTree

from .AbletonComponent import AbletonComponent


class Pan(AbletonComponent):
    lom_id: int
    manual: int
    # midi_controller_range: MidiControllerRange
    # automation_target: AutomationTarget
    # modulation_target: ModulationTarget

    def __init__(self, root: ElementTree.Element):
        super().__init__(root)


class Mixer(AbletonComponent):
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

    def __init__(self, root: ElementTree.Element):
        super().__init__(root)
