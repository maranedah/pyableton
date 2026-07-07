import gzip
import xml.etree.ElementTree as ET

import muspy

from . import extract
from .AbletonComponent import AbletonComponent
from .LiveSet import LiveSet


class Ableton(AbletonComponent):
    """
    Ableton Class

    Represents an Ableton Live project.

    Attributes
    ----------
    major_version : int
        The major version of the Ableton Live project.
    minor_version : str
        The minor version of the Ableton Live project.
    schema_change_count : int
        The schema change count of the Ableton Live project.
    creator : str
        The creator of the Ableton Live project.
    revision : str
        The revision of the Ableton Live project.
    live_set : LiveSet
        The LiveSet object representing the contents of the Ableton Live project.

    """

    major_version: int
    minor_version: str
    schema_change_count: int
    creator: str
    revision: str
    live_set: LiveSet

    def __init__(self, als_file: str):
        """
        Initializes an Ableton instance.

        Parameters
        ----------
        als_file : str
            The path to the Ableton Live Set file (ALS) to be loaded.
        """
        self.als_file = str(als_file)
        self.root = ET.fromstring(self._read_xml())
        super().__init__(self.root)

    def _read_xml(self) -> bytes:
        """Return the decompressed (gunzipped) ALS XML content as bytes."""
        with gzip.open(self.als_file, "rb") as gzipped_file:
            return gzipped_file.read()

    def to_xml(self, filepath: str):
        """
        Converts the Ableton Live Set file to XML format.

        Parameters
        ----------
        filepath : str
            The path to save the XML file.
        """
        with open(filepath, "wb") as output_file:
            output_file.write(self._read_xml())

    def to_muspy(self):
        """
        Converts the Ableton Live Set to MusPy format.

        Reads every MIDI track's full set of arrangement clips (not just the first),
        and builds tempo / time-signature lists from the master track's automation
        (falling back to the manual values). Works across Ableton Live versions.

        Returns
        -------
        muspy.Music
            The MusPy representation of the Ableton Live Set.
        """
        resolution = muspy.DEFAULT_RESOLUTION
        live_set = extract.find_live_set(self.root)

        def to_ticks(beat):
            return int(round(beat * resolution))

        tracks = []
        for track_element in extract.iter_midi_tracks(live_set):
            notes = [
                muspy.Note(
                    time=to_ticks(beat),
                    pitch=int(pitch),
                    duration=max(1, to_ticks(duration)),
                    velocity=max(0, min(127, int(round(velocity)))),
                )
                for beat, pitch, duration, velocity in extract.track_notes(track_element)
            ]
            tracks.append(
                muspy.Track(
                    program=0,
                    is_drum=extract.is_drum_track(track_element),
                    name=extract.track_name(track_element),
                    notes=notes,
                    chords=[],
                    annotations=[],
                    lyrics=[],
                )
            )

        tempos = [
            muspy.Tempo(time=to_ticks(beat), qpm=qpm)
            for beat, qpm in extract.get_tempo_map(live_set)
        ]
        time_signatures = [
            muspy.TimeSignature(time=to_ticks(beat), numerator=num, denominator=den)
            for beat, num, den in extract.get_time_signature_map(live_set)
        ]

        return muspy.Music(
            metadata=muspy.Metadata(),
            resolution=resolution,
            tempos=tempos or [muspy.Tempo(time=0, qpm=120.0)],
            key_signatures=[],
            time_signatures=time_signatures,
            beats=[],
            lyrics=[],
            annotations=[],
            tracks=tracks,
        )

    def to_midi(self, filepath: str):
        self.to_muspy().write_midi(filepath)
