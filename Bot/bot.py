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
for x in os.listdir(os.path.abspath(r'Bot\cogs')) 
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
        
#login,status
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


bot.run(token)
