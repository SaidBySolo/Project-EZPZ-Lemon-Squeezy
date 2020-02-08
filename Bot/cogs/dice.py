import random
from random import randint
import discord
from discord.ext import commands

class Dice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def 주사위(self, ctx, number: int = 100):
        author = ctx.author
        if number > 1:
            n = randint(1, number)
            await ctx.send("{}님이 주사위를 굴려 🎲{}이(가) 나왔어요!".format(author.mention, n))
        else:
            await ctx.send("{}님 1보다 큰 숫자를 주세요.".format(author.mention))

def setup(bot):
    bot.add_cog(Dice(bot))