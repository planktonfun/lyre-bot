import logging
import typing

from discord.ext import commands

log = logging.getLogger(__name__)


class DevClass:
    def __init__(self, content):
        self.content = content

    def __repr__(self) -> str:
        return repr(self.content)


class DevConverter(commands.Converter):
    async def convert(self, ctx, argument):
        log.info(f"argument:\n{argument}")
        return DevClass(argument)


class DevCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=("e",))
    async def echo_input(self, ctx, *, output: typing.Optional[DevConverter]):
        log.info(f"output: {output}")


def setup(bot):
    bot.add_cog(DevCommand(bot))
