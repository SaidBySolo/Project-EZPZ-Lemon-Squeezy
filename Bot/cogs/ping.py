import discord
from discord.ext import commands
import time


class Ping(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        
    @commands.command(pass_context=True)
    async def ping(self,ctx):
        """Martini-ping time"""
        t1 = time.perf_counter()
        async with ctx.typing():
            t2 = time.perf_counter()
        await ctx.send(":ping_pong: Pong! {}ms".format(round((t2-t1)*1000)))

    @commands.command(pass_context=True)
    async def 핑(self,ctx):
        """Korean-Martini-ping time"""
        t1 = time.perf_counter()
        async with ctx.typing():
            t2 = time.perf_counter()
        await ctx.send(":ping_pong: 퐁! {}ms".format(round((t2-t1)*1000)))

def setup(bot):
    bot.add_cog(Ping(bot))

