import discord
import datetime
import random
import BotEmbed
import botToken
from discord.ext import commands

#prefix
bot = commands.Bot(command_prefix='!')

#paste token
token = "NjU3NjA0NDA3MDIxNjY2MzA0.Xf-JVw.Krgxt54ycfRKhRs0oQ5vSf7PLwI"

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

    #commands
@bot.command()
async def 도움말(ctx):
    await ctx.send(embed = BotEmbed.Helps)

async def 제작현황(ctx):
    await ctx.send("제작중")

@bot.command()
async def 내정보(ctx):
    react_embed = (ctx.author.id)
    if react_embed is not None:
        if react_embed == 406430032546889730:
            await ctx.send(embed = BotEmbed.Sabin)
        elif react_embed == 345265069132742657:
                await ctx.send(embed = BotEmbed.SaidBySolo)
        else:
                await ctx.send("임베드가 존재하지않습니다. 관리자에게 문의하여주세요")



bot.run(token)
