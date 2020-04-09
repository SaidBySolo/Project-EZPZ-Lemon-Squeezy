import os
import discord
from discord.ext import commands
import json

with open("Bot/cogs/etc/Auth.json", "r") as Token:
    Auth = json.load(Token)


bot = commands.Bot(command_prefix='&')
bot.remove_command ('help')
token = Auth['token']
bot.load_extension('jishaku')
initial_extensions = ['cogs.' + x[:-3] 
for x in os.listdir('Bot/cogs') 
if x[-3:] == ".py" and not x.startswith("__")]

#cogs
if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)

#reloadall
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
        


bot.run(token)
