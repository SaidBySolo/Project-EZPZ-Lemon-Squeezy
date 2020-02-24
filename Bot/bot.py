import discord
from discord.ext import commands

#prefix
bot = commands.Bot(command_prefix='&')

#remove defalt help command
bot.remove_command ('help')

#paste token
token = "NjU3NjA0NDA3MDIxNjY2MzA0.Xk96RQ.L6v7HCKIdesqrqiiZhdVvK8SSyQ"

#cogs import here
initial_extensions = ['cogs.general',
                    'cogs.lunch',
                    'cogs.vote',
                    'cogs.ping',
                    'cogs.dice',
                    'cogs.nsfw',
                    'cogs.info',
                    'cogs.events',
                    'cogs.qna',
                    'cogs.music',
                    'cogs.admin',
                    'cogs.weather']

#cogs
if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)
#load
@bot.command()
@commands.is_owner()
async def load(ctx, extension):
    try:
        bot.load_extension(extension)
        await ctx.send(f"{extension} 로드 성공.")
    except Exception as e:
        await ctx.send(f"{extension} 로드 실패")
        raise e

#unload
@bot.command()
@commands.is_owner()
async def unload(ctx, extension):
    try:
        bot.unload_extension(extension)
        await ctx.send(f"{extension} 언로드 성공.")
    except Exception as e:
        await ctx.send(f"{extension} 언로드 실패")
        raise e

#reload
@bot.command()
@commands.is_owner()
async def reload(ctx, extension):
    try:
        bot.unload_extension(extension)
        bot.load_extension(extension)
        await ctx.send(f"{extension} 리로드 성공.")
    except Exception as e:
        await ctx.send(f"{extension} 리로드 실패")
        raise e

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

    # Status
    game = discord.Game("v.1.0.1, &도움말")
    await bot.change_presence(status=discord.Status.online, activity=game)

bot.run(token)
