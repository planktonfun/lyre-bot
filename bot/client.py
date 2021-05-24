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

    def load_extensions(self):
        self.load_extension("bot.exts.keymap_reader")
