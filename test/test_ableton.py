import pathlib
import unittest

from pyableton.Ableton import Ableton
from pyableton.AbletonComponent import AbletonComponent
from pyableton.ClipTimeable import ClipTimeable
from pyableton.LiveSet import LiveSet
from pyableton.Midi import DeviceChain, IORouting, MidiName
from pyableton.Mixer import Mixer
from pyableton.Sequencer import FreezeSequencer, MainSequencer
from pyableton.Track import MasterTrack, MidiTrack, Track, TrackDelay


class TestAbleton(unittest.TestCase):
    def setUp(self):
        self.test_path = pathlib.Path(__file__).parent
        self.ableton = Ableton(self.test_path / "test.als")
        self.ableton.to_xml(self.test_path / "test.als", self.test_path / "test_output.xml")
        self.live_set = self.ableton.live_set
        self.midi_track = self.ableton.live_set.tracks[0]
        self.device_chain = self.ableton.live_set.tracks[0].device_chain
        self.main_sequencer = self.ableton.live_set.tracks[0].device_chain.main_sequencer
        self.events = self.main_sequencer.clip_timeable.arranger_automation.events

    def test_ableton_object(self):
        assert self.ableton.major_version == 5
        assert self.ableton.minor_version == "11.0_436"
        assert self.ableton.schema_change_count == 8
        assert self.ableton.creator == "Ableton Live 11.1.5"
        assert self.ableton.revision == "89a839b2c081f06acd48a0dfd5f1007fa7709604"
        assert isinstance(self.ableton.live_set, AbletonComponent)
        assert isinstance(self.ableton.live_set, LiveSet)

    def test_live_set(self):
        assert self.live_set.next_pointee_id == 27102
        assert self.live_set.overwrite_protection_number == 2817
        assert self.live_set.lom_id == 3
        assert self.live_set.lom_id_view == 0
        assert isinstance(self.live_set.tracks, list)
        assert all(isinstance(element, Track) for element in self.live_set.tracks)
        assert len(self.live_set.tracks) == 6
        assert isinstance(self.live_set.master_track, MasterTrack)

    def test_midi_track(self):
        assert isinstance(self.midi_track, MidiTrack)
        assert self.midi_track.id == 12
        assert self.midi_track.lom_id == 0
        assert self.midi_track.lom_id_view == 0
        assert self.midi_track.is_content_selected_in_document is True
        assert self.midi_track.preferred_content_view_mode == 0
        assert isinstance(self.midi_track.track_delay, TrackDelay)
        assert isinstance(self.midi_track.name, MidiName)
        assert self.midi_track.color == 6
        # assert self.midi_track.automation_envelopes
        assert self.midi_track.track_group_id == -1
        assert self.midi_track.track_unfolded is True
        assert self.midi_track.devices_list_wrapper == 0
        assert self.midi_track.clip_slots_list_wrapper == 0
        assert self.midi_track.view_data == {}
        # assert self.midi_track.take_lanes
        assert self.midi_track.linked_track_group_id == -1
        assert self.midi_track.saved_playing_slot == -1
        assert self.midi_track.saved_playing_offset == 0
        assert self.midi_track.freeze is False
        assert self.midi_track.velocity_detail == 0
        assert self.midi_track.need_arranger_refreeze is True
        assert self.midi_track.post_process_freeze_clips == 0
        assert isinstance(self.midi_track.device_chain, DeviceChain)
        assert self.midi_track.re_wire_slave_midi_target_id == 0
        assert self.midi_track.pitchbend_range == 96

    def test_device_chain(self):
        assert self.device_chain.clip_envelope_chooser_view_state.selected_device == 0
        assert self.device_chain.clip_envelope_chooser_view_state.selected_envelope == 0
        assert self.device_chain.clip_envelope_chooser_view_state.prefer_modulation_visible is False
        assert isinstance(self.device_chain.audio_input_routing, IORouting)
        assert isinstance(self.device_chain.audio_output_routing, IORouting)
        assert isinstance(self.device_chain.midi_input_routing, IORouting)
        assert isinstance(self.device_chain.midi_input_routing, IORouting)
        assert isinstance(self.device_chain.mixer, Mixer)
        assert isinstance(self.device_chain.main_sequencer, MainSequencer)
        assert isinstance(self.device_chain.freeze_sequencer, FreezeSequencer)

    def test_main_sequencer(self):
        assert self.main_sequencer.lom_id == 0
        assert self.main_sequencer.lom_id_view == 0
        assert self.main_sequencer.is_expanded is True
        # assert self.main_sequencer.on
        assert self.main_sequencer.modulation_source_count == 0
        assert self.main_sequencer.parameters_list_wrapper == 0
        # assert self.main_sequencer.pointee == 19713
        assert self.main_sequencer.last_selected_timeable_index == 0
        assert self.main_sequencer.last_selected_clip_envelope_index == 0
        # assert self.main_sequencer.last_preset_ref
        # assert self.main_sequencer.locked_scripts is None
        assert self.main_sequencer.is_folded is False
        assert self.main_sequencer.should_show_preset_name is False
        assert self.main_sequencer.user_name == ""
        assert self.main_sequencer.annotation == ""
        # assert self.main_sequencer.source_context
        # assert self.main_sequencer.clip_slot_list
        assert self.main_sequencer.monitoring_enum == 1
        assert isinstance(self.main_sequencer.clip_timeable, ClipTimeable)
        # assert self.main_sequencer.recorder
        # assert self.main_sequencer.midi_controllers

    def test_events(self):
        assert self.events[0] is not None

    def test_notes(self):
        assert self.events[0].notes.get_notes() is not None
        assert self.events[0].notes.to_pandas() is not None

    def test_get_notes(self):
        assert self.ableton.get_notes() is not None
        self.ableton.get_notes().write_midi(self.test_path / "test.midi")

    def test_to_als(self):
        return None

    def test_to_xml(self):
        return None

    def test_midi_tracks(self):
        assert self.ableton.live_set.tracks[0] is not None
