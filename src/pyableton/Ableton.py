import xml.etree.ElementTree as ET

import muspy

from .AbletonComponent import AbletonComponent
from .LiveSet import LiveSet
from .Track import MidiTrack


class Ableton(AbletonComponent):
    major_version: int
    minor_version: str
    schema_change_count: int
    creator: str
    revision: str
    live_set: LiveSet

    def __init__(self, xml_file: str):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        super().__init__(root)

    def get_notes(self):
        midi_tracks = [track for track in self.live_set.tracks if isinstance(track, MidiTrack)]

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

        midi_data = muspy.Music(
            metadata=muspy.Metadata(),
            resolution=muspy.DEFAULT_RESOLUTION,
            tempos=[],
            key_signatures=[],
            time_signatures=[],
            beats=[],
            lyrics=[],
            annotations=[],
            tracks=tracks,
        )
        return midi_data
