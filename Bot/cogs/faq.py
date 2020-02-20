import discord
from discord.ext import commands


class FAQ(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    @commands.dm_only()
    async def on_message(self, message):
        if message.content.startswith("ping"):
            await self.bot.send_message(message.channel, "Pong")


def setup(bot):
    bot.add_cog(FAQ(bot))
