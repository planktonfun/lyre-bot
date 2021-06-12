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
# bpm 40
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
    parser = KeyMapParser()
    result = await parser.get_bpm(raw_content_basic)
    print(parser.has_bpm, parser.bpm, result) # should be False 0 and a filtered string with no bpm in it
    print('=====================================')
    keymap = await parser.get_keymap(raw_content_basic)
    print(keymap) # check if everything is ok
    print('=====================================')
    lines = await KeyMapParser.get_lines(dedent(keymap))
    for line in lines:
        print(line) # check if everything is ok
    print('=====================================')
    notes = await parser.parse_lines(lines)
    for note in notes:
        print(note) # check if everything is ok
    print('=====================================')
    parser = KeyMapParser()
    result = await parser.get_bpm(raw_content_full)
    print(parser.has_bpm, parser.bpm, result) # should be True 375 and a filtered string with no bpm in it
    print('=====================================')
    keymap = await parser.get_keymap(raw_content_full)
    print(keymap) # check if everything is ok
    print('=====================================')
    lines = await KeyMapParser.get_lines(dedent(keymap))
    for line in lines:
        print(line) # check if everything is ok
    print('=====================================')
    notes = await parser.parse_lines(lines)
    for note in notes:
        print(note) # check if everything is ok
    print('=====================================')
    target_string = "EEEEEE[Eqweqwe]EEEE {qweqwe}EEEE EEE EEE   EEE E EEE   EEE EE"
    results = await KeyMapParser.count_keys_by_group(target_string)
    print(results) # should be 34
    print('=====================================')
    target_string = "[ee]EE {EFG} E (FFF) | [FF]FFF[AA](FF)"
    filtered = await KeyMapParser.support_brackets(target_string)
    print(filtered) # () should be converted to []
    print('=====================================')
    target_string = "Do1 Do2 Do3 La1 La2 La3 Ti1 Mi3" # U J M W S X Q B
    filtered = await KeyMapParser.support_solfege(target_string)
    print(filtered) # Notation should be converted to Letters
    print('=====================================')
    await KeyMapParser.get_keymap(raw_content)


asyncio.run(main())