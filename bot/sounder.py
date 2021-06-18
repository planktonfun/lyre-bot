from pydub import AudioSegment
import asyncio

SOUND_MAP = {
    "z": AudioSegment.from_mp3("notes/z.mp3"),
    "x": AudioSegment.from_mp3("notes/x.mp3"),
    "c": AudioSegment.from_mp3("notes/c.mp3"),
    "v": AudioSegment.from_mp3("notes/v.mp3"),
    "b": AudioSegment.from_mp3("notes/b.mp3"),
    "n": AudioSegment.from_mp3("notes/n.mp3"),
    "m": AudioSegment.from_mp3("notes/m.mp3"),
    "a": AudioSegment.from_mp3("notes/a.mp3"),
    "s": AudioSegment.from_mp3("notes/s.mp3"),
    "d": AudioSegment.from_mp3("notes/d.mp3"),
    "f": AudioSegment.from_mp3("notes/f.mp3"),
    "g": AudioSegment.from_mp3("notes/g.mp3"),
    "h": AudioSegment.from_mp3("notes/h.mp3"),
    "j": AudioSegment.from_mp3("notes/j.mp3"),
    "q": AudioSegment.from_mp3("notes/q.mp3"),
    "w": AudioSegment.from_mp3("notes/w.mp3"),
    "e": AudioSegment.from_mp3("notes/e.mp3"),
    "r": AudioSegment.from_mp3("notes/r.mp3"),
    "t": AudioSegment.from_mp3("notes/t.mp3"),
    "y": AudioSegment.from_mp3("notes/y.mp3"),
    "u": AudioSegment.from_mp3("notes/u.mp3"),
}

class Sounder():
    @staticmethod
    async def createFile(notes, filename):
        time_sum = 0

        for note in notes:
            time_sum += note[1]

        soundFile = AudioSegment.silent(duration=time_sum) # or be explicit
        time_sum = 0
        for note in notes:
            print(note[0], time_sum)
            soundFile = soundFile.overlay(SOUND_MAP.get(note[0]), position=time_sum)
            time_sum += note[1]

        soundFile.export(filename, format="mp3")
        return filename