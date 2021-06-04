"""
Load bot configuration from environmental variables.
Missing settings will be populated with defaults defined in this file.
"""
import logging
import os

log = logging.getLogger()


class Env:
    IS_DEV = os.environ.get("IS_DEV_ENV", 0)


class Log:
    LEVEL = os.environ.get("LOG_LEVEL", "INFO")


class Bot:
    PREFIX = os.environ.get("BOT_PREFIX", "~")
    TOKEN = os.environ.get("BOT_TOKEN")


class DejaVu:
    LYRICS = (
        "Déjà vu, I've just been in this place before",
        "Higher on the street, and I know it's my time to go",
        "Calling you, and the search is a mystery",
        "Standing on my feet, it's so hard when I try to be me, woah",
    )
