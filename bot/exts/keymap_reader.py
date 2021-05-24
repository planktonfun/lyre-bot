import logging
import discord
import io

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

    @commands.command()
    async def read(self, ctx, notes: KeyMapParser):
        async with ctx.channel.typing():
            await self.performer.load(notes)
            await self.performer.export(DEFAULT_WAV_PATH)
            with open(DEFAULT_WAV_PATH, "rb") as fp:
                await ctx.send(file=discord.File(fp))


def setup(bot):
    bot.add_cog(KeymapReader(bot))
