import random
from random import randint
import discord
from discord.ext import commands

class Dice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def 주사위(self, ctx, number: int = 6):
        try:
            number = int(number)
        except ValueError:
            await ctx.send("숫자를 입력해주세요")
            return
        author = ctx.author
        if number > 1:
            n = randint(1, number)
            await ctx.send(f"{author.mention}님이 주사위를 굴려 🎲{n}이(가) 나왔어요!")
        else:
            await ctx.send(f"{author.mention}님 1보다 큰 숫자를 주세요.")

def setup(bot):
    bot.add_cog(Dice(bot))
