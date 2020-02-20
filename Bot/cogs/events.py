import discord
from discord.ext import commands

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("명령어를 찾을수없습니다. +도움말을 참조하여 확인해주세요")
    
def setup(bot):
    bot.add_cog(Events(bot))
        