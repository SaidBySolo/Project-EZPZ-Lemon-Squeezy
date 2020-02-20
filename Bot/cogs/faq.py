import discord
from discord.ext import commands


class FAQ(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    @commands.dm_only()
    async def on_message(self, message, ctx):
        if not message.guild:
            await ctx.send("test")
        
def setup(bot):
    bot.add_cog(FAQ(bot))
