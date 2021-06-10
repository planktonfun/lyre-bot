# lyre-bot

[![Build and Deploy to Google Compute Engine](https://github.com/EdmundYuen/lyre-bot/actions/workflows/setup-gcloud.yml/badge.svg)](https://github.com/EdmundYuen/lyre-bot/actions/workflows/setup-gcloud.yml)

Utility bot for the Genshin Lyre Discord server.

## Design Specs

### 1 Play command — Generate audio files from text-formatted key maps

Explanation of the checkboxes below:

- [x] Currently supported
- [ ] Not supported yet

#### 1.1 Invoking the command

- Command prefix:
  - [x] CP1 (Use a mention): `@lyre-bot`
  - [x] CP2 (Use bot command prefix): `~`

- Command name:
  - [x] CN1 (full command name): `play`
  - [x] CN2 (empty string '' as alias): `''`

Supported command invocation styles:

````text
@lyre-bot play
```
key map enclosed in triple backticks codeblock
```
````

````text
@lyre-bot
```
key map enclosed in triple backticks codeblock
```
````

````text
~play
```
key map enclosed in triple backticks codeblock
```
````

````text
~
```
key map enclosed in triple backticks codeblock
```
````

#### 1.2 Formatting the key map to be bot-readable

Pitch formats:

- [x] P1 (PC): Use corresponding PC keyboard keys
  - [x] `[ZXCVBNMASDFGHJQWERTYU]`
  - [x] `[ZzXxCcVvBbNnMmAaSsDdFfGgHhJjQqWwEeRrTtYyUu]`
- [ ] P2 (Solfege): Use corresponding solfege name and octave numbering
  - `(Do|do|Re|re|Mi|mi|Fa|fa|So|so|La|la|Ti|ti)[345]`
- [ ] P3 (Pitch): Use standard pitch notation system
  - `[CcDdEeFfGgAaBb][345]`

Tempo formats:

- [ ] T1 (BPM): Specify beats per minute with positive integer
  - `# (BPM|bpm): ([1-9]\d*)`

Rhythm formats:

- [x] R1 (Even subdivision system): Every grouping (and sub-grouping) has the same length of time

    ```text
    | N  -N MA -F | -D -  -  -  | S - - S F D - A | -N-- -    |
    ```

- [ ] R2 (OG keymap guide): Based on updated instructions in genshin lyre google docs

    ```text
    N | NMA ~F ~D ... S | SFD ~A ~N
    ```

- [ ] R3 (Whitespace): Use whitespace to vertically align and space out notes

    ```text
    #1 2 3 4  1 2 3 4  1 2 3 4  1 2 3 4
    |N  NMA F| D      |S  SFD A| N      |
    ```

Multi-notes / Chords:

- [ ] Arppegios: play notes smoothly and quickly one after the other

  - e.g. `{ZBADGQ}`

- [ ] Chords: play more than one note at the same time

  - e.g. `(ADG) (SGJ) (ADH) (MDG)`

- [ ] Trills: alternate between two adjacent notes

  - e.g. `| A  Q  | Q~ -J |` (play Q~ as WQWQWQWQ)

- [ ] Tremolo: play same note many times

- [ ] Multiple parts: duets/trios/quartets

    ```text
    Mandolin 1 | EE  WQ  W~  -   Q   -   -   -   |
    Mandolin 2 | QQ  JE  J~  -   Q   -   -   -   |
    Strings    | Z   Z   B   B   Z   -   -   -   |
    ```

Performance instructions:

- [ ] Specify verse/chorus sections
- [ ] Notating repeats

## Instructions for local development (Linux/WSL)

Work in progress..

### Pre-requisites

1. Python 3.9
2. Various build dependencies
3. Pipenv

### Installation

```bash
git clone https://github.com/EdmundYuen/lyre-bot.git
cd lyre-bot/
export INSTALLATION_DIR=$(pwd)
pipenv install
```

### Runtime configuration

Export the following environmental variables or create a .env file.

```bash
export IS_DEV_ENV=1
export BOT_TOKEN="bot token from discord developer portal"
export BOT_PREFIX="!"
export PYTHONPATH=$PYTHONPATH:$INSTALLATION_DIR
```

Run the bot with `pipenv run python3 -m bot`

Check container deployment with `docker-compose up -d --build` and clean up with `docker-compose down`.

## Development wishlist

1. Key map parsing

   1. Fix rhythm bugs
   2. Recognise chords
   3. Case-insensitive
   4. Smarter handling of unrecognised characters
   5. Allow for comments in the key map
   6. Recognise arpeggios/trills
   7. Add support for notation similar to updated guide
   8. Add support for multiple parts

2. Key Map Formatter/Prettifier

   1. Alignment and whitespace
   2. Autofill rests when time signature is given

3. Parsing of additional information

   1. Tempo / Time signature
   2. Metadata (links, composer, transcriber, etc)

4. Message output

   1. Use embeds for prettier look and display provided metadata
   2. Add qiqi image to go with qiqi.wav

5. Bot usability

   1. Provide key map template through help command or when encountering conversion errors
   2. Error handling for command not found error (need newline between @lyre-bot and ```)
   3. Better documentation, tips and tricks for getting your desired output from the bot

6. CI/CD

   1. Dockerise and host on GCP Compute Engine free tier for 24/7 availability
   2. Setup GitHub actions for build test publish deploy pipeline
   3. Write a contributing.md?
   4. Use pytest
   5. Refactor existing code into testable units based on design specs

7. Lyre / Audio Synthesis

   1. Upload audio output as compressed format instead of wav
   2. Find out why current mixing method has performance issues
   3. Match tuning of in-game harp as much as possible
   4. Explore alternatives for better synthesised/non-synthesised lyre sounds
