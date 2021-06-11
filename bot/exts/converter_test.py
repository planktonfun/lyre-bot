import asyncio
from textwrap import dedent

from bot.exts.converter import KeyMapParser
from bot.exts.lyre import Note

raw_content_basic = """~read
```
| ZBADGQ | XBMSGJ | CNADH  | CBMDG  |
| ZVNAF  | ZBADG  | VNASH  | XVBMSG |
| zbadgq | xbmsgj | cnadh  | cbmdg  |
| zvnaf  | zbadg  | vnash  | xvbmsg |
```"""

raw_content_full = """~read
```
# bpm 123
| E E E | [ee]EE {EFG} E | [FF]FFF[AA](FF) | GGGGGGGG  |
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

    print('=====================================')
    result = await KeyMapParser.get_bpm(raw_content_basic)
    print(KeyMapParser.has_bpm, KeyMapParser.bpm, result) # should be 0 0 and a filtered string with no bpm in it
    print('=====================================')
    keymap = await KeyMapParser.get_keymap(raw_content_basic)
    print(keymap) # check if everything is ok
    print('=====================================')
    result = await KeyMapParser.get_bpm(raw_content_full)
    print(KeyMapParser.has_bpm, KeyMapParser.bpm, result) # should be 1 121.9512 aand a filtered string with no bpm in it
    print('=====================================')
    keymap = await KeyMapParser.get_keymap(raw_content_full)
    print(keymap) # check if everything is ok
    print('=====================================')
    lines = await KeyMapParser.get_lines(dedent(keymap))
    for line in lines:
        print(line) # check if everything is ok
    print('=====================================')
    notes = await KeyMapParser.parse_lines(lines)
    for note in notes:
        print(note) # check if everything is ok
    print('=====================================')
    target_string = "EEEEEE[Eqweqwe]EEEE {qweqwe}EEEE EEE EEE   EEE E EEE   EEE EE"
    results = await KeyMapParser.count_keys_by_group(target_string)
    print(results) # should be 34
    print('=====================================')
    await KeyMapParser.get_keymap(raw_content)


asyncio.run(main())
