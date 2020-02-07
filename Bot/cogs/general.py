from .etc.botembed import BotEmbed
from .etc.userdict import UserDict
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

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(":ping_pong:Pong!")

    @commands.command()
    async def 핑(self, ctx):
        await ctx.send(":ping_pong:퐁! ")

    #Information command
    @commands.command()
    async def 내정보(self, ctx):
        react_embed = UserDict.user_embed.get(ctx.author.id)
        if react_embed is not None: 
            await ctx.send(embed = react_embed)
        else:
            await ctx.send("엠베드가 존재하지않슴니다. 관리자에게 문의해주세요")
def setup(bot):
    bot.add_cog(General(bot))