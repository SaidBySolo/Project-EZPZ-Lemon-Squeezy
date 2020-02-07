import discord
from discord.ext import commands

#prefix
bot = commands.Bot(command_prefix='!')

#remove defalt help command
bot.remove_command ('help')

#paste token
token = "NjU3NjA0NDA3MDIxNjY2MzA0.Xf-JVw.Krgxt54ycfRKhRs0oQ5vSf7PLwI"

#cogs import here
initial_extensions = ['cogs.general',
                    'cogs.lunch',
                    'cogs.vote']

#cogs
if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)

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
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("명령어를 찾을수없습니다. !도움말을 참조하여 확인해주세요")
    
bot.run(token)
