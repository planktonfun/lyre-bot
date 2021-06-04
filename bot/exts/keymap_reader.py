import logging
import random

import discord
from discord import Embed
from discord.ext import commands

from bot.constants import DejaVu
from bot.exts.converter import KeyMapParser, STANDARD_LINE_DURATION
from bot.exts.lyre import Lyre, Performer

log = logging.getLogger(__name__)

DEFAULT_WAV_PATH = "qiqi.wav"


def create_embed(ctx: commands.Context):
    author = ctx.author
    notes = ctx.args[-1]
    notes_repr = "".join(
        f"{note.pitch:2} /{STANDARD_LINE_DURATION/note.duration:4n} | "
        if i % 4 != 3
        else f"{note.pitch:2} /{STANDARD_LINE_DURATION/note.duration:4n}\n"
        for i, note in enumerate(notes)
    )
    if len(notes_repr) > 2042:
        notes_repr = notes_repr[:2038] + "\n..."
    description = f"```{notes_repr}```"
    return Embed(
        title="Lyre Bot Player",
        description=description,
        color=author.colour,
    ).set_footer(text=random.choice(DejaVu.LYRICS))


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
                await ctx.send(embed=create_embed(ctx), file=discord.File(fp))

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
