import logging

import discord
from discord.ext import commands
from exts.converter import KeyMapParser
from exts.lyre import Lyre, Performer

log = logging.getLogger(__name__)

DEFAULT_WAV_PATH = "qiqi.wav"


class KeymapReader(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.lyre = Lyre.create()
        self.performer = Performer(self.lyre)

    @commands.command(aliases=("p", ""))
    async def play(self, ctx, notes: KeyMapParser):
        async with ctx.channel.typing():
            await self.performer.load(notes)
            await self.performer.export(DEFAULT_WAV_PATH)
            with open(DEFAULT_WAV_PATH, "rb") as fp:
                await ctx.send(file=discord.File(fp))

    @play.error
    async def play_error(self, ctx, error):
        if isinstance(error, commands.ConversionError):
            await ctx.send("Keymap conversion failed.")
        elif isinstance(error, commands.CommandInvokeError):
            if isinstance(error.original, discord.HTTPException):
                await ctx.send("File upload has failed. The keymap might be too long.")
            else:
                await ctx.send(error)
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(
                "I did not detect any keymaps. Please surround your keymap with \\`\\`\\` \\`\\`\\`"
            )
        else:
            await ctx.send(error)
        raise error


def setup(bot):
    bot.add_cog(KeymapReader(bot))
