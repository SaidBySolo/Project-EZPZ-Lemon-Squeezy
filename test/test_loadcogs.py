import discord
from discord.ext import commands
import sys,os
os.path.abspath(os.path.join(os.path.dirname(__file__),os.pardir))

def load_cogs():
    bot = commands.Bot(command_prefix='!')
    extensions = []
    for file in os.listdir("cogs"):
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

def test_load_cogs():
    bot = commands.Bot(command_prefix='!')
    failed_cogs = load_cogs()
    assert(len(failed_cogs) == 0)
    
