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


def get_bot_instance(is_dev: int) -> LyreBot:
    if is_dev:
        bot_instance = LyreBot.create_for_dev()
        bot_instance.load_extensions_for_dev()
        return bot_instance
    else:
        bot_instance = LyreBot.create()
        bot_instance.load_extensions()
        return bot_instance


def main(args: Namespace):
    setup_logger()
    bot.instance = get_bot_instance(args.is_dev)
    bot.instance.run(args.bot_token)


if __name__ == "__main__":
    main(args)
