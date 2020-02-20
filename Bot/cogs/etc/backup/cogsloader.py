import discord
from discord.ext import commands

initial_extensions = ['cogs.general',
                    'cogs.lunch',
                    'cogs.vote',
                    'cogs.ping',
                    'cogs.dice',
                    'cogs.nsfw',
                    'cogs.info',
                    'cogs.cogsloader']


class CogsLoader(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

def setup(bot):
    bot.add_cog(CogsLoader(bot))
        