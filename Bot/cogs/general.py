from .etc.botembed import BotEmbed
import discord
from discord.ext import commands

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #commands
    @commands.command()
    async def 도움말(self, ctx):
        await ctx.send(embed = BotEmbed.Helps)

    @commands.command()
    async def 제작현황(self, ctx):
        await ctx.send("제작중")

    #Information command
    #Hello
    @commands.command()
    async def 안녕(self,ctx):
        await ctx.send("안녕하세요!")

    @commands.command()
    async def 링크(self, ctx):
        await ctx.send("https://discordapp.com/api/oauth2/authorize?client_id=657604407021666304&permissions=391232&scope=bot")

def setup(bot):
    bot.add_cog(General(bot))