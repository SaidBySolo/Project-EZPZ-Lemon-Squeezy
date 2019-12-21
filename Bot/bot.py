import discord
from discord.ext import commands

token = "NjU3NjA0NDA3MDIxNjY2MzA0.XfzoCQ.3OBZ_60-CcPyaZcC-uGW9SLHOIo"

#command_prefix
bot = commands.Bot(command_prefix='!')

@bot.event        
        #Login
async def on_ready():
    print("login.... ")
    print(bot.user.name)
    print(bot.user.id)
    print("======================")

@bot.command()
async def test(ctx):
    await ctx.send('OK')

bot.run(token)
