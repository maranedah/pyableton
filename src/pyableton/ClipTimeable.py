from xml.etree import ElementTree

from .AbletonComponent import AbletonComponent
from .ViewStates import AutomationTransformViewState


class MidiClip(AbletonComponent):
    id: int
    time: int
    lom_id: int
    lom_id_view: int
    current_start: int
    current_end: int
    # loop: Loop
    name: str
    annotation: str
    color: int
    launch_mode: int
    launch_quantisation: int
    # time_signature: list[TimeSignature]
    # envelopes: list[Envelope]
    # scroller_time_preserver: ScrollerTimePreserver
    # time_selection: TimeSelection
    legato: bool
    ram: bool
    # groove_settings: GrooveSettings
    disabled: bool
    velocity_amount: int
    # follow_action: FollowAction
    # grid: Grid
    freeze_start: int
    freeze_end: int
    is_warped: bool
    take_id: int
    # notes: Content
    bank_select_coarse: int
    bank_select_fine: int
    program_change: int
    note_editor_fold_in_zoom: int
    note_editor_fold_in_scroll: int
    note_editor_fold_out_zoom: int
    note_editor_fold_out_scroll: int
    note_editor_fold_scale_zoom: int
    note_editor_fold_scale_scroll: int
    # scale_information: ScaleInformation
    is_in_key: bool
    note_spelling_preference: int
    prefer_flat_root_note: bool
    # expression_grid: ExpressionGrid

    def __init__(self, root: ElementTree.Element):
        super().__init__(root)


class ArrangerAutomation(AbletonComponent):
    events: list[MidiClip]
    automation_transform_view_state: AutomationTransformViewState

    def __init__(self, root: ElementTree.Element):
        super().__init__(root)


class ClipTimeable(AbletonComponent):
    arranger_automation: ArrangerAutomation

    def __init__(self, root: ElementTree.Element):
        super().__init__(root)
