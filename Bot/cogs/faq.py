import discord
from discord.ext import commands


class FAQ(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if not message.guild:
            await message.channel.send("Test")
        
def setup(bot):
    bot.add_cog(FAQ(bot))
