import discord
import datetime
import random
import BotEmbed
import botToken
#from discord.ext import commands

#prefix(무기한연장)
#bot = commands.Bot(command_prefix='!')

#Client
client = discord.Client()

#paste token
token = "NjU3NjA0NDA3MDIxNjY2MzA0.Xf-JVw.Krgxt54ycfRKhRs0oQ5vSf7PLwI"

@client.event
async def on_ready():
    # login
    print("Login.. : ")
    print(bot.user.name)
    print(bot.user.id)
    print("======================")

    # Status message
    game = discord.Game("v.1.0.0, !도움말")
    await client.change_presence(status=discord.Status.online, activity=game)


    #need Prefix work.
    #commands
@client.event
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
    JH_id = 587245907029000205

    #my information
    if message.content == "!내정보":
        if message.author.id == Sabin_id:
            await message.channel.send(embed = BotEmbed.Sabin)

    if message.content == "!내정보":
        if message.author.id == SBS_id:
            await message.channel.send(embed = BotEmbed.SaidBySolo)

    if message.content == "!내정보":
        if message.author.id == Huggy_id:
            await message.channel.send(embed = BotEmbed.Huggy)

    if message.content == "!내정보":
        if message.author.id == Bliz_id:
            await message.channel.send(embed = BotEmbed.Bliz)

    if message.content == "!내정보":
        if message.author.id == Decfcone1_id:
            await message.channel.send(embed = BotEmbed.Decfcone1)

    if message.content == "!내정보":
        if message.author.id == JH_id:
            await message.channel.send(embed = BotEmbed.JH)

client.run(token)
