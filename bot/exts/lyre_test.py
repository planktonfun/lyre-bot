import asyncio

from exts.lyre import Lyre, Note, Performer


async def aiter_notes(notes):
    for note in notes:
        yield note


test_notes = aiter_notes(
    [
        Note("C3", 1e3),
        Note("D3", 0.5e3),
        Note("E3", 0.5e3),
        Note("F3", 1e3),
        Note("G3", 1e3),
        Note("R", 1e3),
        Note("A3", 1e3),
        Note("B3", 1e3),
        Note("C4", 1e3),
        Note("D4", 0.5e3),
        Note("E4", 0.5e3),
        Note("F4", 1e3),
        Note("G4", 1e3),
        Note("R", 1e3),
        Note("A4", 1e3),
        Note("B4", 1e3),
        Note("C5", 1e3),
        Note("D5", 0.5e3),
        Note("E5", 0.5e3),
        Note("F5", 1e3),
        Note("G5", 1e3),
        Note("R", 1e3),
        Note("A5", 1e3),
        Note("B5", 1e3),
        Note("C5", 0.5e3),
        Note("E5", 0.5e3),
        Note("D5", 0.5e3),
        Note("C5", 0.5e3),
        Note("B4", 0.5e3),
        Note("A4", 0.5e3),
        Note("C5", 0.5e3),
        Note("E4", 0.5e3),
        Note("C4", 0.5e3),
        Note("B3", 0.5e3),
        Note("D5", 0.5e3),
        Note("B4", 0.5e3),
        Note("A4", 0.5e3),
        Note("C4", 0.5e3),
        Note("A3", 0.5e3),
        Note("B3", 0.5e3),
        Note("E4", 0.5e3),
        Note("D4", 0.5e3),
        Note("C4", 0.5e3),
        Note("D4", 0.5e3),
        Note("F4", 0.5e3),
        Note("E4", 0.5e3),
        Note("E4", 0.5e3),
        Note("G4", 0.5e3),
        Note("F4", 0.5e3),
        Note("F4", 0.5e3),
        Note("E4", 0.5e3),
        Note("D4", 0.5e3),
        Note("E4", 0.5e3),
        Note("D4", 0.5e3),
        Note("E4", 0.5e3),
        Note("C5", 0.5e3),
        Note("E4", 0.5e3),
        Note("G4", 0.5e3),
        Note("B4", 0.5e3),
        Note("G4", 0.5e3),
        Note("E4", 0.5e3),
        Note("E5", 0.5e3),
        Note("C5", 0.5e3),
        Note("E5", 0.5e3),
        Note("C5", 0.5e3),
        Note("B4", 0.5e3),
        Note("A4", 0.5e3),
        Note("A4", 0.5e3),
        Note("B4", 0.5e3),
        Note("C5", 0.5e3),
        Note("C5", 0.5e3),
        Note("E5", 0.5e3),
        Note("F5", 0.5e3),
        Note("A4", 0.5e3),
        Note("A4", 0.5e3),
        Note("G4", 0.5e3),
        Note("D4", 0.5e3),
        Note("G4", 0.5e3),
        Note("R", 1e3),
    ]
)

test_same_notes = aiter_notes(
    [
        Note("C4", 0.4e3),
        Note("C4", 0.4e3),
        Note("C3", 0.4e3),
        Note("C5", 0.4e3),
        Note("C4", 0.4e3),
        Note("C4", 0.4e3),
        Note("C3", 0.4e3),
        Note("C5", 0.4e3),
        Note("C4", 0.4e3),
        Note("C4", 0.4e3),
        Note("C3", 0.4e3),
        Note("C5", 0.4e3),
        Note("R", 1e3),
    ]
)


wav_path = "test.wav"
wav_path_2 = "test2.wav"


async def perform():
    lyre = Lyre.create()
    performer = Performer(lyre)
    await performer.load(test_notes)
    await performer.export(wav_path)
    await performer.load(test_same_notes)
    await performer.export(wav_path_2)


async def main():
    asyncio.create_task(perform())


asyncio.run(main())
