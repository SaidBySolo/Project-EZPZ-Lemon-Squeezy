from .etc.botembed import BotEmbed
import discord
from discord.ext import commands
import asyncio

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

    @commands.command()
    async def 개발진(self, ctx):
        await ctx.send(embed = BotEmbed.Dev)

    @commands.command()  
    async def 문의(self, ctx):
        await ctx.send("문의는 저에게 DM!")

    #Hello
    @commands.command()
    async def 안녕(self,ctx):
        await ctx.send("안녕하세요!")

    @commands.command()
    async def 링크(self, ctx):
        link = "https://discordapp.com/api/oauth2/authorize?client_id=657604407021666304&permissions=70773824&scope=bot"
        await ctx.send(f"{link}")

def setup(bot):
    bot.add_cog(General(bot))