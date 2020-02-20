from .etc.botembed import BotEmbed
import datetime
import discord
from discord.ext import commands

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    now = datetime.datetime.now()

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

    @commands.command()
    async def 내정보(self,ctx):
            joindate = datetime.datetime.utcfromtimestamp(((int(ctx.author.id) >> 22) + 1420070400000) / 1000)
            info = discord.Embed(title="Info", description=f"{ctx.author.name}님의 정보입니다", color=0x569271)
            info.set_thumbnail(url=ctx.author.avatar_url)
            info.add_field(name="Server Nickname", value=f"{ctx.author.display_name}", inline=False)
            info.add_field(name="DID", value=f"{ctx.author.id}", inline=False)
            info.add_field(name="Joined", value= f"{str(joindate.year)}년 {str(joindate.month)}월 {str(joindate.day)}일 {str(joindate.hour)}시 {str(joindate.minute)}분 {str(joindate.second)}초", inline=False)
            info.add_field(name="Contact Information",value=ctx.author, inline=False)
            await ctx.send(embed = info)

            
def setup(bot):
    bot.add_cog(General(bot))