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

KEYMAP_MARKER = r"```(\n*.*)*```"
LINE_DIVIDERS = r"[\|\n]"
STANDARD_LINE_DURATION = 2e3


class KeyMapParser(commands.Converter):
    async def convert(self, ctx, _) -> List[Note]:
        keymap = await KeyMapParser.get_keymap(ctx.message.content)
        lines = await KeyMapParser.get_lines(keymap)
        notes = await KeyMapParser.parse_lines(lines)
        return notes

    @staticmethod
    async def get_keymap(content: str) -> str:
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

    @staticmethod
    async def parse_lines(lines: List[List[str]]) -> List[Note]:
        notes = []
        for line in lines:
            n_words = len(line)
            for word in line:
                n_keys = len(word)
                for key in word:
                    pitch = KEY_MAP.get(key, "R")
                    duration = STANDARD_LINE_DURATION / (n_words * n_keys)
                    notes.append(Note(pitch=pitch, duration=duration))
        return notes
