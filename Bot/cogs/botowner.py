import discord
from discord.ext import commands

class Botowner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def load(self, ctx, extension):
        try:
            self.bot.load_extension(extension)
            await ctx.send(f"{extension} 로드 성공.")
        except Exception as e:
            await ctx.send(f"{extension} 로드 실패")
            raise e

    #unload
    @commands.command()
    @commands.is_owner()
    async def unload(self, ctx, extension):
        try:
            self.bot.unload_extension(extension)
            await ctx.send(f"{extension} 언로드 성공.")
        except Exception as e:
            await ctx.send(f"{extension} 언로드 실패")
            raise e

    #reload
    @commands.command()
    @commands.is_owner()
    async def reload(self, ctx, extension):
        try:
            self.bot.unload_extension(extension)
            self.bot.load_extension(extension)
            await ctx.send(f"{extension} 리로드 성공.")
        except Exception as e:
            await ctx.send(f"{extension} 리로드 실패")
            raise e

def setup(bot):
    bot.add_cog(Botowner(bot))