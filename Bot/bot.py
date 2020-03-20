import os
import discord
from discord.ext import commands
from cogs.etc.Auth import Auth

bot = commands.Bot(command_prefix='&')

#remove defalt help command
bot.remove_command ('help')

#paste token
token = Auth.token

#debug
bot.load_extension('jishaku')

#cogs
def load_cogs(bot):
    initial_extensions = ['cogs.' + x[:-3] for x in os.listdir("./Bot/cogs") if x[-3:] == ".py" and not x.startswith("__")]
    failed = []
    if __name__ == '__main__':
        for extension in initial_extensions:
            try:
                bot.load_extension(extension)
            except Exception as e:
                print(f"{e.__class__.__name__} : {str(e)}")
                failed.append(extension)
            if failed:
                print("\n{}로드실패\n".format(" ".join(failed)))
            return failed
       
#reloadall
@bot.command()
@commands.is_owner()
async def reloadall(ctx):
    initial_extensions = ['cogs.' + x[:-3] for x in os.listdir("./Bot/cogs") if x[-3:] == ".py" and not x.startswith("__")]
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

if __name__ == '__main__':
    # Changing current working directory to use relative directories
    current_file_dir = os.path.dirname(os.path.realpath(__file__))
    load_cogs(bot)
    os.chdir(current_file_dir)  
    bot.run(token)
