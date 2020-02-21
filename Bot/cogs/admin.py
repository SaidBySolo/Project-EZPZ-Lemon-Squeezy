import asyncio
import discord
from discord.ext import commands

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def 삭제(self, ctx, number: int = 2):
        author = ctx.author
        if number < 100:
            await ctx.channel.purge(limit = number + 1)
            delmsg = await ctx.send(f"{author.mention}님이 메시지{number}개를삭제했어요")
            await asyncio.sleep(5)
            await delmsg.delete()
        else:
            delmsg2 = await ctx.send(f"{author.mention}님이 제한을 초과했습니다.")
            await asyncio.sleep(5)
            await delmsg2.delete()

def setup(bot):
    bot.add_cog(Admin(bot))