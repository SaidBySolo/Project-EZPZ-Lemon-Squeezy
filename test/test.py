import discord
from discord.ext import commands
import sys
sys.path.append('..')
from ..Bot import bot

def testcogs():
    tsbot = commands.Bot(command_prefix='&')
    failed_cogs = bot.load_cogs(tsbot)
    assert(len(failed_cogs) == 0)
