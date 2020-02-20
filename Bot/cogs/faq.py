import discord
from discord.ext import commands


class FAQ(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if not message.guild and message.author.id != 657604407021666304:
            await message.channel.send(f"{message.author.id},{message.author.name},{message.author}")
        
def setup(bot):
    bot.add_cog(FAQ(bot))
