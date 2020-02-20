import datetime
import discord
from discord.ext import commands

class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def 내정보(self,ctx):
        joindate = datetime.datetime.utcfromtimestamp(((int(ctx.author.id) >> 22) + 1420070400000) / 1000)
        now = datetime.datetime.now()
        info = discord.Embed(title="Info", description=f"{ctx.author.name}님의 정보입니다", color=0x569271)
        info.set_thumbnail(url=ctx.author.avatar_url)
        info.add_field(name="Server Nickname", value=f"{ctx.author.display_name}", inline=False)
        info.add_field(name="DID", value=f"{ctx.author.id}", inline=False)
        info.add_field(name="Joined", value= f"{str(joindate.year)}년 {str(joindate.month)}월 {str(joindate.day)}일 {str(joindate.hour)}시 {str(joindate.minute)}분 {str(joindate.second)}초", inline=False)
        info.add_field(name="Contact Information",value=ctx.author, inline=False)
        info.set_footer(text=f"ver:1.0.1 {str(now.year)}년 {str(now.month)}월 {str(now.day)}일 {str(now.hour)}시 {str(now.minute)}분 {str(now.second)}초")
        await ctx.send(embed = info)
            
def setup(bot):
    bot.add_cog(Info(bot))
