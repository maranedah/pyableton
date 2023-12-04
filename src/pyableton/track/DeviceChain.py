from xml.etree import ElementTree

from ..AbletonComponent import AbletonComponent
from .AutomationLane import AutomationLane
from .ClipEnvelopeChooserViewState import ClipEnvelopeChooserViewState
from .FreezeSequencer import FreezeSequencer
from .IORouting import AudioInputRouting, AudioOutputRouting, MidiInputRouting, MidiOutputRouting
from .MainSequencer import MainSequencer
from .Mixer import Mixer


class DeviceChain(AbletonComponent):
    automation_lanes: list[AutomationLane]
    clip_envelope_chooser_view_state: ClipEnvelopeChooserViewState
    audio_input_routing: AudioInputRouting
    midi_input_routing: MidiInputRouting
    audio_output_routing: AudioOutputRouting
    midi_output_routing: MidiOutputRouting
    mixer: Mixer
    main_sequencer: MainSequencer
    freeze_sequencer: FreezeSequencer
    # devices: List[InstrumentGroupDevice]
    # signal_modulations: List[SignalModulation]
    # re_wire_slave_midi_target_id: ReWireSlaveMidiTargetId
    # pitchbend_range: PitchbendRange

    def __init__(self, root: ElementTree.Element):
        # breakpoint()
        super().__init__(root)
