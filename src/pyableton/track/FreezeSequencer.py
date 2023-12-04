from xml.etree import ElementTree

from ..AbletonComponent import AbletonComponent


class FreezeSequencer(AbletonComponent):
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

    def __init__(self, root: ElementTree.Element):
        super().__init__(root)
