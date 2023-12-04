from xml.etree import ElementTree

from ..AbletonComponent import AbletonComponent


class InstrumentGroupDevice(AbletonComponent):
    id: int
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
    # locked_scripts: List[LockedScript]
    is_folded: bool
    should_show_preset_name: bool
    user_name: str
    annotation: str
    # source_context: SourceContext
    overwrite_protection_number: int
    # branches: List[InstrumentBranch]
    is_branches_list_visible: bool
    is_return_branches_list_visible: bool
    is_ranges_editor_visible: bool
    are_devices_visible: bool
    num_visible_macro_controls: int
    # quizas hacer un atributo que se llame macros y asignarles propiedades mejor
    # macro_controls: List[MacroControl]
    # macro_display_names: List[MacroDisplayNames]
    # macro_defaults: List[MacroDefault]
    # macro_annotations: List[str]
    # force_display_generic_value: List[bool]
    are_macro_controls_visible: bool
    is_auto_select_enabled: bool
    # chain_selector: ChainSelector
    # chain_selector_relative_position: ChainSelectorRelativePosition
    views_to_restore_when_unfolding: int
    # return_branches: List[ReturnBranch]
    branches_splitter_proportion: float
    show_branches_in_session_mixer: bool
    # macro_color: List[int]
    lock_id: int
    lock_seal: int
    chains_list_wrapper: int
    return_chains_list_wrapper: int
    # macro_variations: List[MacroSnapShots]
    # exclude_macro_from_randomization: List[bool]
    # exclude_macro_from_snapshots: List[bool]
    are_macro_variations_controls_visible: bool
    chain_selector_filter_midi_ctrl: bool
    range_type_index: int
    shows_zones_inestead_of_note_names: bool

    def __init__(self, root: ElementTree.Element):
        super().__init__(root)
