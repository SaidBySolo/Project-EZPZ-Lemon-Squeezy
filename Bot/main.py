import os
import discord
from discord.ext import commands
import json

with open(r"Bot\cogs\etc\Auth.json", "r") as Token:
    Auth = json.load(Token)

prefix = "&"
token = Auth["token"]

class Bot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, command_prefix=prefix, **kwargs)
        self.prefix = prefix

def initialize(bot_class=Bot):
    bot = bot_class()
    bot.remove_command ('help')
    bot.load_extension('jishaku')
    initial_extensions = ['cogs.' + x[:-3] 
                        for x in os.listdir(r"C:\Users\Administrator\Documents\GitHub\Project-EZPZ-Lemon-Squeezy\Bot\cogs") 
                        if x[-3:] == ".py" and not x.startswith("__")]

    @bot.command()
    @commands.is_owner()
    async def reloadall(ctx):
        for extension in initial_extensions:
            try:
                bot.unload_extension(extension)
                bot.load_extension(extension)
                await ctx.send(f"{extension} 리로드 성공.")
            except Exception as e:
                await ctx.send(f"{extension} 리로드 실패")
                raise e

    @bot.event
    async def on_ready():
        # login
        print("Login.. : ")
        print(bot.user.name)
        print(bot.user.id)
        print("======================")
        print(f"{discord.version_info}")
        print(f"{len(set(bot.get_all_members()))}명이 사용중.")
        print("======================")

        # Status
        game = discord.Game("&도움말 | DM으로 문의 받는중 | Alpha v1.1.1")
        await bot.change_presence(status=discord.Status.online, activity=game)

    return bot

def load_cogs(bot):
    extensions = []
    for file in os.listdir(r"C:\Users\Administrator\Documents\GitHub\Project-EZPZ-Lemon-Squeezy\Bot\cogs"):
        if file.endswith(".py") and not file.startswith("__init__"):
            extensions.append(file.split('.')[0])
    failed = []
    for extension in extensions:
        try:
            bot.load_extension(f"cogs.{extension}")
        except Exception as e:
            print(f"{e.__class__.__name__}: {str(e)}")
            failed.append(extension)
    if failed:
        print(f'\n{" ".join(failed)}로드실패\n')
    return failed

if __name__ == '__main__':
    # Changing current working directory to use relative directories
    current_file_dir = os.path.dirname(os.path.realpath(__file__))
    os.chdir(current_file_dir)
    bot = initialize()
    load_cogs(bot)
    bot.run(token)
