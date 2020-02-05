import discord
import datetime
import random
import asyncio
import json
import os
from discord.ext import commands


token = "NjU3NjA0NDA3MDIxNjY2MzA0.Xf-JVw.Krgxt54ycfRKhRs0oQ5vSf7PLwI"
des="Martini"
prefix="!"

class Bot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, command_prefix=prefix, **kwargs)#Prefix
        self.prefix = prefix
        
def initialize(bot_class=Bot):
    bot = bot_class(description=des)

#remove defalt help command
    bot.remove_command ('help')

#login,status
    @bot.event
    async def on_ready():
        # login
        print("Login.. : ")
        print(bot.user.name)
        print(bot.user.id)
        print("======================")

    # Status
        game = discord.Game("v.1.0.1, !도움말")
        await bot.change_presence(status=discord.Status.online, activity=game)

#command not found
    @bot.event
    async def on_command_error(ctx, error):
        channel = ctx.message.channel
        if isinstance(error, commands.CommandNotFound):
            await bot.send_message(channel,"명령어를 찾을수없습니다. !도움말을 참조하여 확인해주세요")

    return bot

def load_cogs(bot):
    extensions = []
    for file in os.listdir("./cogs"):
        if file.endswith(".py") and not file.startswith("__init__"):
            extensions.append(file.split('.')[0])
    failed = []
    for extension in extensions:
        try:
            bot.load_extension("cogs.{}".format(extension))
        except Exception as e:
            print("{}: {}".format(e.__class__.__name__, str(e)))
            failed.append(extension)
    if failed:
        print("\n{}항목 로드 실패.\n".format(" ".join(failed)))
    return failed

if __name__ == '__main__':
    current_file_dir = os.path.dirname(os.path.realpath(__file__))
    os.chdir(current_file_dir)
    bot = initialize()
    load_cogs(bot)
    bot.run(token)

    