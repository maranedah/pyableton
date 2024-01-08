import muspy

from .AbletonComponent import AbletonComponent


class AutomationTransformViewState(AbletonComponent):
    """
    AutomationTransformViewState Class

    Represents the view state for automation transformation.

    Attributes
    ----------
    is_transform_pending : bool
        Flag indicating whether automation transformation is pending.

    """

    is_transform_pending: bool


class MidiNoteEvent(AbletonComponent):
    """
    MidiNoteEvent Class

    Represents a MIDI note event.

    Attributes
    ----------
    time : float
        The time position of the MIDI note event.
    duration : float
        The duration of the MIDI note event.
    velocity : int
        The velocity of the MIDI note event.
    velocity_deviation : int
        The velocity deviation of the MIDI note event.
    off_velocity : int
        The off velocity of the MIDI note event.
    probability : float
        The probability of the MIDI note event.
    is_enabled : bool
        Flag indicating whether the MIDI note event is enabled.
    note_id : int
        The ID of the MIDI note.

    Methods
    -------
    __str__()
        Returns a string representation of the MidiNoteEvent.

    """

    time: float
    duration: float
    velocity: int
    velocity_deviation: int
    off_velocity: int
    probability: float
    is_enabled: bool
    note_id: int

    def __str__(self):
        """
        Returns a string representation of the MidiNoteEvent.

        Returns
        -------
        str
            String representation of the MidiNoteEvent.

        """
        return f"MidiNoteEvent(time={self.time}, \
            duration={self.duration}, velocity={self.velocity})"


class KeyTrack(AbletonComponent):
    """
    KeyTrack Class

    Represents a key track.

    Attributes
    ----------
    id : int
        The ID of the key track.
    notes : list[MidiNoteEvent]
        List of MIDI note events in the key track.
    midi_key : int
        The MIDI key of the key track.

    Methods
    -------
    get_notes()
        Returns a list of muspy.Note objects derived from the key track.

    """

    id: int
    notes: list[MidiNoteEvent]
    midi_key: int

    def get_notes(self):
        """
        Returns a list of muspy.Note objects derived from the key track.

        Returns
        -------
        list[muspy.Note]
            List of muspy.Note objects.

        """
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
    """
    Notes Class

    Represents a collection of key tracks.

    Attributes
    ----------
    key_tracks : list[KeyTrack]
        List of key tracks.

    Methods
    -------
    get_notes()
        Returns a sorted list of muspy.Note objects derived from all key tracks.
    to_pandas()
        Returns a pandas DataFrame representation of the note data.

    """

    key_tracks: list[KeyTrack]

    def get_notes(self):
        """
        Returns a sorted list of muspy.Note objects derived from all key tracks.

        Returns
        -------
        list[muspy.Note]
            List of muspy.Note objects.

        """
        notes = [note for key_track in self.key_tracks for note in key_track.get_notes()]
        notes.sort(key=lambda x: (x.time, x.pitch, x.duration))
        return notes

    def to_pandas(self):
        """
        Returns a pandas DataFrame representation of the note data.

        Returns
        -------
        pd.DataFrame
            Pandas DataFrame containing note data.

        """
        import pandas as pd

        notes = [vars(note) for key_track in self.key_tracks for note in key_track.get_notes()]
        df = pd.DataFrame(notes).sort_values(by=["time", "pitch", "duration"])
        df = df.reset_index(drop=True)
        return df


class MidiClip(AbletonComponent):
    """
    MidiClip Class

    Represents a MIDI clip in Ableton.

    Attributes
    ----------
    id : int
        The unique identifier of the MIDI clip.
    time : int
        The time position of the MIDI clip.
    lom_id : int
        The Level of Mess (LOM) ID associated with the MIDI clip.
    lom_id_view : int
        The LOM ID view of the MIDI clip.
    current_start : int
        The current start time of the MIDI clip.
    current_end : int
        The current end time of the MIDI clip.
    name : str
        The name of the MIDI clip.
    annotation : str
        The annotation of the MIDI clip.
    color : int
        The color code of the MIDI clip.
    launch_mode : int
        The launch mode of the MIDI clip.
    launch_quantisation : int
        The launch quantization setting of the MIDI clip.
    legato : bool
        Flag indicating whether legato mode is enabled for the MIDI clip.
    ram : bool
        Flag indicating whether RAM mode is enabled for the MIDI clip.
    disabled : bool
        Flag indicating whether the MIDI clip is disabled.
    velocity_amount : int
        The velocity amount setting for the MIDI clip.
    freeze_start : int
        The start time for freezing the MIDI clip.
    freeze_end : int
        The end time for freezing the MIDI clip.
    is_warped : bool
        Flag indicating whether the MIDI clip is warped.
    take_id : int
        The unique identifier of the take associated with the MIDI clip.
    notes : Notes
        The notes associated with the MIDI clip.
    bank_select_coarse : int
        The coarse value of the bank select MIDI controller.
    bank_select_fine : int
        The fine value of the bank select MIDI controller.
    program_change : int
        The program change value for the MIDI clip.
    note_editor_fold_in_zoom : int
        The zoom setting for folding in the note editor.
    note_editor_fold_in_scroll : int
        The scroll setting for folding in the note editor.
    note_editor_fold_out_zoom : int
        The zoom setting for folding out in the note editor.
    note_editor_fold_out_scroll : int
        The scroll setting for folding out in the note editor.
    note_editor_fold_scale_zoom : int
        The zoom setting for folding the scale in the note editor.
    note_editor_fold_scale_scroll : int
        The scroll setting for folding the scale in the note editor.
    is_in_key : bool
        Flag indicating whether the MIDI clip is in key.
    note_spelling_preference : int
        The preference for note spelling in the MIDI clip.
    prefer_flat_root_note : bool
        Flag indicating whether a flat root note is preferred in the MIDI clip.

    """

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
    """
    ArrangerAutomation Class

    Represents automation events in the arranger.

    Attributes
    ----------
    events : list[MidiClip]
        List of MIDI clips associated with the arranger automation.
    automation_transform_view_state : AutomationTransformViewState
        The view state for automation transformation in the arranger.

    """

    events: list[MidiClip]
    automation_transform_view_state: AutomationTransformViewState


class ClipTimeable(AbletonComponent):
    """
    ClipTimeable Class

    Represents a timeable clip in Ableton.

    Attributes
    ----------
    arranger_automation : ArrangerAutomation
        The arranger automation associated with the timeable clip.

    """

    arranger_automation: ArrangerAutomation
