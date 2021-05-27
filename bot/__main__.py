import logging
from argparse import Namespace

import bot
from bot import constants
from bot.client import LyreBot
from bot.logs import setup_logger

log = logging.getLogger("bot")

args = Namespace(
    is_dev=constants.Env.IS_DEV,
    bot_token=constants.Bot.TOKEN,
)


def get_bot_instance(is_dev):
    if is_dev:
        return LyreBot.create_for_dev()
    else:
        return LyreBot.create()


def main(args):
    setup_logger()
    bot.instance = get_bot_instance(args.is_dev)
    bot.instance.load_extensions()
    bot.instance.run(args.bot_token)


if __name__ == "__main__":
    main(args)
