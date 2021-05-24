"""
Setup Python logging configuration.
"""
import logging

from bot import constants

log = logging.getLogger()


def setup_logger():
    logging.basicConfig(level=constants.Log.LEVEL)
    logging.getLogger("discord").setLevel(logging.WARNING)
