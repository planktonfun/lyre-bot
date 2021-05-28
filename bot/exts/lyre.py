import logging
import random
from collections import namedtuple
from typing import List

from gensound import Fade, Gain, Signal, Silence, Sine
from gensound.transforms import Stretch

log = logging.getLogger(__name__)

# fmt: off
PITCHES = [
    "C3", "D3", "E3", "F3", "G3", "A3", "B3",
    "C4", "D4", "E4", "F4", "G4", "A4", "B4",
    "C5", "D5", "E5", "F5", "G5", "A5", "B5",
    "R"
]
# fmt: on

Note = namedtuple("Note", ["pitch", "duration"])
Tone = namedtuple("Tone", ["f", "f2", "f3"])
ToneMap = namedtuple("ToneMap", PITCHES)


class Lyre:
    TONES = ToneMap(
        Tone(125, 258, 389),
        Tone(147, 287, 438),
        Tone(164, 324, 494),
        Tone(177, 347, 523),
        Tone(195, 397, 587),
        Tone(222, 445, 664),
        Tone(246, 495, 745),
        Tone(269, 527, 788),
        Tone(297, 584, 882),
        Tone(326, 660, 994),
        Tone(355, 703, 1051),
        Tone(395, 786, 1178),
        Tone(438, 877, 1315),
        Tone(494, 994, 1486),
        Tone(530, 1050, 1574),
        Tone(585, 1180, 1766),
        Tone(664, 1299, 1990),
        Tone(703, 1402, 2101),
        Tone(784, 1570, 2348),
        Tone(878, 1764, 2633),
        Tone(992, 1969, 2968),
        Tone(None, None, None),
    )

    RESONANCE_DURATION = 1e3
    FADE_DURATION = 7e2
    SECOND_OVERTONE_GAIN = Gain(-40)
    THIRD_HARMONIC_GAIN = Gain(-60)
    TUNING = 1
    MODULATION = 0.001

    def __init__(self):
        self.buffer = Silence(0)

    @classmethod
    def create(cls):
        tones = cls.TONES._asdict()
        cls.PITCH_MAP = {pitch: cls.get_signal(tone) for pitch, tone in tones.items()}
        return cls()

    @staticmethod
    def get_signal(tone: Tone) -> Signal:
        f = Sine(frequency=tone.f, duration=Lyre.RESONANCE_DURATION)
        f2 = (
            Sine(frequency=tone.f2, duration=Lyre.RESONANCE_DURATION)
            * Lyre.SECOND_OVERTONE_GAIN
        )
        f3 = (
            Sine(frequency=tone.f3, duration=Lyre.RESONANCE_DURATION)
            * Lyre.THIRD_HARMONIC_GAIN
        )
        combined_signal = sum((f, f2, f3))
        return combined_signal * Fade(is_in=False, duration=Lyre.FADE_DURATION)

    async def play(self, note: Note) -> Signal:
        signal = Lyre.PITCH_MAP.get(note.pitch, Silence(0))
        rate = random.gauss(mu=Lyre.TUNING, sigma=Lyre.MODULATION)
        signal *= Stretch(rate=rate)
        mixed_signal = self.buffer + signal
        self.buffer = mixed_signal[:, note.duration :]
        return mixed_signal[:, : note.duration]

    async def simple_play(self, note: Note) -> Signal:
        signal = Lyre.PITCH_MAP.get(note.pitch, Silence(0))
        rate = random.gauss(mu=Lyre.TUNING, sigma=Lyre.MODULATION)
        signal *= Stretch(rate=rate)
        fade_duration = 0.3 * min(Lyre.RESONANCE_DURATION, note.duration)
        signal = signal[:, : note.duration] * Fade(is_in=False, duration=fade_duration)
        return signal

    async def clear_buffer(self):
        self.buffer = Silence(0)


class Performer:
    def __init__(self, instrument):
        self.wav = None
        self.instrument = instrument

    async def load(self, notes: List[Note]):
        aiter_notes = self.aiter_notes(notes)
        note_len = len(notes)
        if note_len > 50:
            self.wav = Signal.concat(
                [await self.simple_play_note(note) async for note in aiter_notes]
            )
        else:
            self.wav = Signal.concat(
                [await self.play_note(note) async for note in aiter_notes]
            )
        await self.instrument.clear_buffer()

    async def play_note(self, note: Note) -> Signal:
        return await self.instrument.play(note)

    async def simple_play_note(self, note: Note) -> Signal:
        return await self.instrument.simple_play(note)

    async def export(self, path: str):
        if self.wav is None:
            raise AttributeError
        else:
            self.wav.export(path)

    @staticmethod
    async def aiter_notes(notes: List[Note]):
        for note in notes:
            yield note
