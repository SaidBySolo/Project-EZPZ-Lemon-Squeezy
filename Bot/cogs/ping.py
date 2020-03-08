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
        pingingembed = discord.Embed(title="Pinging....", description = "Wait a Second....")
        editpinging = await ctx.send(embed = pingingembed)
        latency = round(self.bot.latency * 1000)        
        msglatency = round((t2-t1)*1000)
        pingembed = discord.Embed(color=0x218362, title=":ping_pong: Pong!", description = f"Web Soket Delay\n{latency}ms\n\nFinal delay(Up to chat)\n{msglatency}ms")
        await editpinging.edit(embed=pingembed)

def setup(bot):
    bot.add_cog(Ping(bot))

