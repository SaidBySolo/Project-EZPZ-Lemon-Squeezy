import discord
from discord.ext import commands
import time


class Ping(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        
    @commands.command(pass_context=True)
    async def ping(self,ctx):
        t1 = time.perf_counter()
        async with ctx.typing():
            t2 = time.perf_counter()
        await ctx.send(f":ping_pong: Pong! {(round((t2-t1)*1000))}ms")

    @commands.command(pass_context=True)
    async def 핑(self,ctx):
        t1 = time.perf_counter()
        async with ctx.typing():
            t2 = time.perf_counter()
        await ctx.send(f":ping_pong: 퐁! {(round((t2-t1)*1000))}ms")

def setup(bot):
    bot.add_cog(Ping(bot))

