import gzip
import os
import xml.etree.ElementTree as ET

import muspy

from .AbletonComponent import AbletonComponent
from .constants import TIME_SIGNATURE_IDS
from .LiveSet import LiveSet
from .Track import MidiTrack


class Ableton(AbletonComponent):
    major_version: int
    minor_version: str
    schema_change_count: int
    creator: str
    revision: str
    live_set: LiveSet

    def __init__(self, als_file: str):
        self.als_file = als_file
        filepath = "temp.xml"
        self.to_xml(filepath)
        tree = ET.parse(filepath)
        os.remove(filepath)
        root = tree.getroot()
        super().__init__(root)

    def to_xml(self, filepath: str):
        with gzip.open(self.als_file, "rb") as gzipped_file:
            xml_content = gzipped_file.read()
        with open(filepath, "wb") as output_file:
            output_file.write(xml_content)

    def to_muspy(self):
        midi_tracks = [
            track
            for track in self.live_set.tracks
            if isinstance(track, MidiTrack)
        ]
        tracks = [
            muspy.Track(
                program=0,
                is_drum="drum"
                in (
                    midi_track.device_chain.main_sequencer.clip_timeable.arranger_automation.events[
                        0
                    ].name
                ).lower(),
                name=(
                    midi_track.device_chain.main_sequencer.clip_timeable.arranger_automation.events[
                        0
                    ].name
                ),
                notes=(
                    midi_track.device_chain.main_sequencer.clip_timeable.arranger_automation.events[
                        0
                    ].notes.get_notes()
                ),
                chords=[],
                annotations=[],
                lyrics=[],
            )
            for midi_track in midi_tracks
        ]
        time_signatures_automation = (
            self.live_set.master_track
            .automation_envelopes
            .envelopes[0]
            .automation.events
        )
        midi_data = muspy.Music(
            metadata=muspy.Metadata(),
            resolution=muspy.DEFAULT_RESOLUTION,
            tempos=[
                muspy.Tempo(
                    time=0 * muspy.DEFAULT_RESOLUTION,
                    qpm=self.live_set.master_track.device_chain.mixer.tempo.manual,
                )
            ],
            key_signatures=[],
            time_signatures=[
                muspy.TimeSignature(
                    time=max(0, time_signature_event.time * muspy.DEFAULT_RESOLUTION),
                    numerator=TIME_SIGNATURE_IDS[time_signature_event.value]["numerator"],
                    denominator=TIME_SIGNATURE_IDS[time_signature_event.value]["denominator"],
                )
                for time_signature_event in time_signatures_automation
            ],
            beats=[],
            lyrics=[],
            annotations=[],
            tracks=tracks,
        )
        return midi_data
