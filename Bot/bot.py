import discord
import datetime
import random

client = discord.Client()

token = "Token"


@client.event
async def on_ready():
    # Login
    print("login.... ")
    print(client.user.name)
    print(client.user.id)
    print("======================")

@client.event
async def on_message(message):
    if message.content == ("안녕?"):
        await message.channel.send("안녕! :smile:")

client.run(token)
