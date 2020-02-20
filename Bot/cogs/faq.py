import discord
from discord.ext import commands


class FAQ(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    @commands.dm_only()
    async def on_message(self, ctx, message):
        if message.content.startswith("ping"):
            await ctx.send(message.channel, "Pong")


def setup(bot):
    bot.add_cog(FAQ(bot))
