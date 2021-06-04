import logging

import discord
from discord.ext import commands

from bot import constants

log = logging.getLogger("bot")


class LyreBot(commands.Bot):
    async def on_ready(self):
        log.info("Logged in as %s", self.user)

    async def on_command(self, ctx):
        log.info("Command invoked: %s - %s", ctx.command, ctx.author)

    @classmethod
    def create(cls) -> "LyreBot":
        """Create and return an instance of a LyreBot."""
        return cls(
            command_prefix=commands.when_mentioned_or(constants.Bot.PREFIX),
            activity=discord.Game(name=f"Commands: {constants.Bot.PREFIX}help"),
        )

    @classmethod
    def create_for_dev(cls) -> "LyreBot":
        """Create and return an instance of a LyreBot for development and testing."""
        return cls(
            command_prefix=constants.Bot.PREFIX,
            status=discord.Status.do_not_disturb,
        )

    def load_extensions(self):
        self.load_extension("bot.exts.keymap_reader")

    def load_extensions_for_dev(self):
        self.load_extension("bot.exts.keymap_reader")
        self.load_extension("bot.exts.dev_utils")
