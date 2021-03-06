import discord
from discord.ext import commands

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #login,status
    @commands.Cog.listener()
    async def on_ready(self):
        # login
        print("Login.. : ")
        print(self.bot.user.name)
        print(self.bot.user.id)
        print("======================")
        print(f"{len(set(self.bot.get_all_members()))}명이 사용중.")
        print("======================")

        # Status
        game = discord.Game("&도움말 | DM으로 문의 받는중 | Alpha v1.1.1")
        await self.bot.change_presence(status=discord.Status.online, activity=game)


    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("명령어를 찾을수없습니다. &도움말을 참조하여 확인해주세요", delete_after=5)

        elif isinstance(error, commands.BadArgument):
            await ctx.send('명령어의 인자가 부족합니다. &도움말을 참조하여 확인해주세요', delete_after=5)

        elif isinstance(error, commands.DisabledCommand):
            await ctx.send('비활성화된 명령어 입니다', delete_after=5)

def setup(bot):
    bot.add_cog(Events(bot))
        
