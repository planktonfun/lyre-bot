import asyncio
from textwrap import dedent

from exts.converter import KeyMapParser
from exts.lyre import Note

raw_content = """~read
```
| ZBADGQ | XBMSGJ | CNADH  | CBMDG  |
| ZVNAF  | ZBADG  | VNASH  | XVBMSG |
```"""

test_text = dedent(
    """
    | QQE QQE QQE QQH JJE JJE JJE JJE |
    | Q E W Q J   - H HHJ QWE H   -   |
    """
)

test_raw_lines = [
    " QQE QQE QQE QQH JJE JJE JJE JJE ",
    " Q E W Q J   - H HHJ QWE H   -   ",
]

test_lines = [
    ["QQE", "QQE", "QQE", "QQH", "JJE", "JJE", "JJE", "JJE"],
    ["Q", "E", "W", "Q", "J", "-", "H", "HHJ", "QWE", "H", "-"],
]

test_notes = [
    Note("C5", 1e3 / 3),
    Note("C5", 1e3 / 3),
    Note("E5", 1e3 / 3),
    Note("C5", 1e3 / 3),
    Note("C5", 1e3 / 3),
    Note("E5", 1e3 / 3),
    Note("C5", 1e3 / 3),
    Note("C5", 1e3 / 3),
    Note("E5", 1e3 / 3),
    Note("C5", 1e3 / 3),
    Note("C5", 1e3 / 3),
    Note("A4", 1e3 / 3),
    Note("B4", 1e3 / 3),
    Note("B4", 1e3 / 3),
    Note("E5", 1e3 / 3),
    Note("B4", 1e3 / 3),
    Note("B4", 1e3 / 3),
    Note("E5", 1e3 / 3),
    Note("B4", 1e3 / 3),
    Note("B4", 1e3 / 3),
    Note("E5", 1e3 / 3),
    Note("B4", 1e3 / 3),
    Note("B4", 1e3 / 3),
    Note("E5", 1e3 / 3),
    Note("C5", 1e3),
    Note("E5", 1e3),
    Note("D5", 1e3),
    Note("C5", 1e3),
    Note("B4", 1e3),
    Note("R", 1e3),
    Note("A4", 1e3),
    Note("A4", 1e3 / 3),
    Note("A4", 1e3 / 3),
    Note("B4", 1e3 / 3),
    Note("C5", 1e3 / 3),
    Note("D5", 1e3 / 3),
    Note("E5", 1e3 / 3),
    Note("A4", 1e3),
    Note("R", 1e3),
]


async def main():

    # lines = KeyMapParser.get_lines(test_text)
    # for line in lines:
    #     print(line)

    # for line, test_line in zip(lines, test_lines):
    #     assert line == test_line

    # notes = KeyMapParser.parse_lines(lines)
    # for note in notes:
    #     print(note)

    # for note, test_note in zip(notes, test_notes):
    #     assert note == test_note

    await KeyMapParser.get_keymap(raw_content)


asyncio.run(main())
