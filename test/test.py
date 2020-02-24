import os
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='&')

#cogs import here
initial_extensions = ['cogs.' + x[:-3] for x in os.listdir("Bot/cogs") if x[-3:] == ".py" if x[-3:] == ".py" and not x.startswith("__")]

def test_load_cogs():
	if __name__ == '__main__':
		for extension in initial_extensions:
			try:
				bot.load_extension(extension)
				print(f"{extension} 로드 성공.")
				assert(len(extension) == 0)
			except Exception as e:
				print(f"{extension} 로드 실패")
				raise e



