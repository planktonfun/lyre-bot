import logging
import re
from typing import List

from discord.ext import commands

from bot.exts.lyre import Note

log = logging.getLogger(__name__)

KEY_MAP = {
    "z": "C3",
    "x": "D3",
    "c": "E3",
    "v": "F3",
    "b": "G3",
    "n": "A3",
    "m": "B3",
    "a": "C4",
    "s": "D4",
    "d": "E4",
    "f": "F4",
    "g": "G4",
    "h": "A4",
    "j": "B4",
    "q": "C5",
    "w": "D5",
    "e": "E5",
    "r": "F5",
    "t": "G5",
    "y": "A5",
    "u": "B5",
    "Z": "C3",
    "X": "D3",
    "C": "E3",
    "V": "F3",
    "B": "G3",
    "N": "A3",
    "M": "B3",
    "A": "C4",
    "S": "D4",
    "D": "E4",
    "F": "F4",
    "G": "G4",
    "H": "A4",
    "J": "B4",
    "Q": "C5",
    "W": "D5",
    "E": "E5",
    "R": "F5",
    "T": "G5",
    "Y": "A5",
    "U": "B5",
    "-": "R",
}

BPM_CAPTURE = r"#\s?(BPM|bpm):?\s?(\d+)"
BRACKET_GROUPING = r"((\{\w+\})|(\[\w+\])|\w)"
KEYMAP_MARKER = r"```(\n*.*)*```"
LINE_DIVIDERS = r"[\|\n]"
STANDARD_LINE_DURATION = 2e3
ZERO_DELAY = 10

class KeyMapParser(commands.Converter):
    def __init__(self):
        self.inside_curly = False
        self.inside_bracket = False
        self.use_last_duration = False
        self.last_duration = 0
        self.has_bpm = False
        self.bpm = 0

    async def convert(self, ctx, _):
        keymap = await KeyMapParser.get_keymap(ctx.message.content)
        lines = await KeyMapParser.get_lines(keymap)
        notes = await KeyMapParser.parse_lines(lines)
        return notes

    @staticmethod
    async def support_brackets(content: str) -> str:
        content = re.sub(r"\(", '[', content)
        content = re.sub(r"\)", ']', content)
        return content

    async def get_bpm(self, content: str) -> str:
        pattern = re.compile(BPM_CAPTURE)
        for match in pattern.finditer(content):
            self.bpm = 60000/float(match.group(2))/4
            self.has_bpm = True

        if(self.has_bpm == True):
            return re.sub(BPM_CAPTURE, '', content)

        return content

    async def get_keymap(self, content: str) -> str:
        content = await self.get_bpm(content)
        content = await KeyMapParser.support_brackets(content)
        keymap_match = re.search(KEYMAP_MARKER, content)
        if keymap_match:
            return keymap_match.group().strip("`")
        else:
            raise ValueError

    @staticmethod
    async def get_lines(keymap: str) -> List[List[str]]:
        candidates = re.split(LINE_DIVIDERS, keymap)
        raw_lines = filter(lambda x: x != "", candidates)
        lines = [line.strip().split() for line in raw_lines]
        return lines

    async def calculate_duration(self, duration: float, words: int, keys: int) -> float:
        if (self.use_last_duration == 1):
            self.use_last_duration = 0
            return self.last_duration
        if (self.inside_bracket == True):
            return ZERO_DELAY
        if (self.inside_curly == True):
            return self.last_duration/2
        if (self.has_bpm == 1):
            return self.bpm
        else:
            return duration / (words * keys)

    async def calculate_last_duration(self, index: int, wordarray):
        if(index+1 < len(wordarray)):
            if (wordarray[index+1] == "]"):
                self.use_last_duration = 1
                if(index+2 == len(wordarray)):
                    self.last_duration += self.bpm
            if (wordarray[index+1] == "}"):
                self.use_last_duration = 1
                if(index+2 == len(wordarray)):
                    self.last_duration += self.bpm
        return 0

    async def calculate_pause_duration(self, index: int, wordlen: int):
        if(self.has_bpm == True):
            if(index+1 == wordlen):
                return self.bpm
        return 0

    @staticmethod
    async def count_keys_by_group(word):
        pattern = re.compile(BRACKET_GROUPING)
        matches = [];
        for match in pattern.finditer(word):
            matches.append(match.group(1))
        return len(matches)

    async def parse_lines(self, lines: List[List[str]]):
        notes = []
        for line in lines:
            n_words = len(line)
            for word in line:
                n_keys = await KeyMapParser.count_keys_by_group(word)
                for idx, key in enumerate(word):
                    await self.calculate_last_duration(idx, word);
                    if (key == "{"):
                        self.last_duration = await self.calculate_duration(STANDARD_LINE_DURATION, n_words, n_keys)
                        self.inside_curly = True
                    elif (key == "}"):
                        self.inside_curly = False
                    elif (key == "["):
                        self.last_duration = await self.calculate_duration(STANDARD_LINE_DURATION, n_words, n_keys)
                        self.inside_bracket = True
                    elif (key == "]"):
                        self.inside_bracket = False
                    else:
                        duration = await self.calculate_duration(STANDARD_LINE_DURATION, n_words, n_keys)
                        duration += await self.calculate_pause_duration(idx, len(word))
                        pitch = KEY_MAP.get(key, "R")
                        notes.append(Note(pitch=pitch, duration=duration))
        return notes
