"""
Load bot configuration from environmental variables.
Missing settings will be populated with defaults defined in this file.
"""
import logging
import os

log = logging.getLogger()


class Log:
    LEVEL = os.environ.get("LOG_LEVEL", "INFO")


class Bot:
    PREFIX = os.environ.get("BOT_PREFIX", "~")
    TOKEN = os.environ.get("BOT_TOKEN")
