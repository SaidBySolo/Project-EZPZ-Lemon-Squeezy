import discord
from discord.ext import commands
import time


class Ping(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        
    @commands.command(aliases=['핑'])
    async def ping(self,ctx):
        t1 = time.perf_counter()
        async with ctx.typing():
            t2 = time.perf_counter()
        await ctx.send(f":ping_pong: Pong! {(round((t2-t1)*1000))}ms")

def setup(bot):
    bot.add_cog(Ping(bot))

