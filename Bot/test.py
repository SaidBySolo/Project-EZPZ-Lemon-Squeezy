import os
import discord
import sys
from discord.ext import commands

bot = commands.Bot(command_prefix='&')

initial_extensions = ['cogs.' + x[:-3] for x in os.listdir("Bot/cogs") if x[-3:] == ".py" if x[-3:] == ".py" and not x.startswith("__")]

if __name__ == '__main__':
    for extension in initial_extensions:
            bot.load_extension(extension)