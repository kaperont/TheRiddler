import logging

import discord
from discord.ext import commands

from ..services import RiddleService

logger = logging.getLogger(__name__)


class Riddle(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(name='riddle', description = 'Track the specified user\'s stats.')
    async def riddle(self, ctx):
        data: dict = RiddleService.get_riddle()
        msg = f'**Riddle:** {data.get("riddle", "No Riddle Found!")}\r\n**Answer:** ||{data.get("answer", "No Answer Found!")}||'

        logger.debug(msg)
        await ctx.respond(msg)


def setup(bot: commands.Bot):
    bot.add_cog(Riddle(bot))
