import muspy

from .AbletonComponent import AbletonComponent
from .ViewStates import AutomationTransformViewState


class MidiNoteEvent(AbletonComponent):
    time: float
    duration: float
    velocity: int
    velocity_deviation: int
    off_velocity: int
    probability: float
    is_enabled: bool
    note_id: int

    def __str__(self):
        return f"MidiNoteEvent(time={self.time}, \
            duration={self.duration}, velocity={self.velocity})"


class KeyTrack(AbletonComponent):
    id: int
    notes: list[MidiNoteEvent]
    midi_key: int

    def get_notes(self):
        return [
            muspy.Note(
                time=int(note.time * muspy.DEFAULT_RESOLUTION),
                pitch=self.midi_key,
                duration=int(note.duration * muspy.DEFAULT_RESOLUTION),
                velocity=note.velocity,
            )
            for note in self.notes
        ]


class Notes(AbletonComponent):
    key_tracks: list[KeyTrack]

    def get_notes(self):
        notes = [note for key_track in self.key_tracks for note in key_track.get_notes()]
        notes.sort(key=lambda x: (x.time, x.pitch, x.duration))
        return notes

    def to_pandas(self):
        import pandas as pd

        notes = [vars(note) for key_track in self.key_tracks for note in key_track.get_notes()]
        df = pd.DataFrame(notes).sort_values(by=["time", "pitch", "duration"])
        df = df.reset_index(drop=True)
        return df


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
    notes: Notes
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


class ArrangerAutomation(AbletonComponent):
    events: list[MidiClip]
    automation_transform_view_state: AutomationTransformViewState


class ClipTimeable(AbletonComponent):
    arranger_automation: ArrangerAutomation
