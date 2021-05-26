import logging

import bot
from bot import constants
from bot.client import LyreBot
from bot.logs import setup_logger

log = logging.getLogger("bot")

if constants.Env.IS_DEV:
    bot.instance = LyreBot.create_for_dev()
else:
    bot.instance = LyreBot.create()


def main():
    setup_logger()
    bot.instance.load_extensions()
    bot.instance.run(constants.Bot.TOKEN)


if __name__ == "__main__":
    main()
