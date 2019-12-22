import discord
import datetime
import random
import BotEmbed

client = discord.Client()

token = "NjU3NjA0NDA3MDIxNjY2MzA0.XfzoCQ.3OBZ_60-CcPyaZcC-uGW9SLHOIo"


@client.event
async def on_ready():
    # login
    print("다음으로 로그인합니다 : ")
    print(client.user.name)
    print(client.user.id)
    print("======================")

    # 상태메시지 표시
    #game0 = discord.Game("")
    #await client.change_presence(status=discord.Status.online, activity=game0)

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

    if message.content == "!내정보":
        if message.author.id == Sabin_id:
            await message.channel.send(embed = BotEmbed.Sabin)

    if message.content == "!내정보":
        if message.author.id == SBS_id:
            await message.channel.send(embed = BotEmbed.SaidBySolo)

client.run(token)
