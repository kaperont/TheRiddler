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
        logger.debug(data)
        
        embed = discord.Embed(
            title='The Riddle',
            description=data.get('riddle', 'No Riddle Found!'),
            color=discord.Colour.yellow()
        )
        embed.add_field(name='Answer', value=f'||{data.get("answer", "No Answer Found!")}||')
        embed.set_footer(text='Riddles provided by Riddles API (https://riddles-api.vercel.app/)')

        await ctx.respond(embed=embed)


def setup(bot: commands.Bot):
    bot.add_cog(Riddle(bot))
