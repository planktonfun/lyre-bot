import asyncio
from pydub import AudioSegment
from pydub.utils import make_chunks
from converter import KeyMapParser

sound1 = AudioSegment.from_mp3("notes/a.mp3")
sound2 = AudioSegment.from_mp3("notes/b.mp3")

# mix sound2 with sound1, starting at 5000ms into sound1)
output = sound1.overlay(sound2, position=5000)
output = output.overlay(sound2, position=500)
output = output.overlay(sound2, position=500)

# save the result
output.export("mixed_sounds.mp3", format="mp3")
print('hello')

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

notes = [
	['a',1000],
	['b',1000],
	['c',1000],
	['d',1000],
	['e',1000],
];

class Sounder():
    @staticmethod
    async def createFile(notes, filename):
        time_sum = 0

        for note in notes:
            time_sum += note[1]

        soundFile = AudioSegment.silent(duration=time_sum) # or be explicit
        # make_chunks(soundFile, time_sum)
        # print('making chunks', time_sum)
        time_sum = 0
        for note in notes:
            print(note[0], time_sum)
            soundFile = soundFile.overlay(SOUND_MAP.get(note[0]), position=time_sum)
            time_sum += note[1]

        soundFile.export(filename, format="mp3")
        return filename

raw_content_basic = """~read
```
#bpm 40

b [sj] [ah] [qd] [js][mg][ah][zsj]ad [xsh] n

b [sj] [ah] [qd] [js][mg][ah][zsj]ad q{xnsh}

w [bu]sjuyt[be]d[qt] y [wb]sj bdagn

[aw] [bu]sjuyt[be]d[qt] y [wb]s[jt]gw bg{dq}j[js]h

{xgu}bm[su][yb][tm][ze]c[dt]cay[wxm]bsgbszbagba

{zju}bm[ua][yg][ta][ex]a[tg] {adgy}{bmst}
```"""

async def main():
	parser = KeyMapParser()
	notes  = await parser.convert(raw_content_basic)
	# await Sounder.play(notes);
	await Sounder.createFile(notes, 'new_file.mp3');

asyncio.run(main())