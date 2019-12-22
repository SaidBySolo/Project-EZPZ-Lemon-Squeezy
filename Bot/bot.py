import discord
import datetime
import random
import BotEmbed
from discord.ext import commands

 #prefix
bot = commands.Bot(command_prefix='!')

 #paste token
token = "token"

@bot.event
async def on_ready():
    # login
    print("Login.. : ")
    print(bot.user.name)
    print(bot.user.id)
    print("======================")

    # Status message
    game0 = discord.Game("v.1.0.0")
    await bot.change_presence(status=discord.Status.online, activity=game0)


    #need Prefix work.
    #commands
@bot.event
async def on_message(message):

    if message.author.bot:
        return None
    if message.content == ("안녕"):
        await message.channel.send("안녕! :smile:")

    if message.content == ("!도움말"):
        await message.channel.send(embed = BotEmbed.Helps)

    if message.content == ("!제작현황"):
        await message.channel.send("제작중")

    #user id variable
    Sabin_id = 406430032546889730
    Huggy_id = 263643715401285632
    SBS_id = 345265069132742657
    Bliz_id = 268334477720289281
    Decfcone1_id = 315373718568173568

    #my information
    if message.content == "!내정보":
        if message.author.id == Sabin_id:
            await message.channel.send(embed = BotEmbed.Sabin)

    if message.content == "!내정보":
        if message.author.id == SBS_id:
            await message.channel.send(embed = BotEmbed.SaidBySolo)

bot.run(token)
