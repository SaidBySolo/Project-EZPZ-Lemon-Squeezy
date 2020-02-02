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

#User Embed
user_embed = {
406430032546889730: BotEmbed.Sabin,
345265069132742657: BotEmbed.SaidBySolo,
263643715401285632: BotEmbed.Huggy,
268334477720289281: BotEmbed.Bliz,
259286662117326848: BotEmbed.Unoh03,
}

#Information command
@bot.command()
async def 내정보(ctx):
    react_embed = user_embed.get(ctx.author.id)
    if react_embed is not None: 
        await ctx.send(embed = react_embed)
    else:
        await ctx.send("엠베드가 존재하지않슴니다. 관리자에게 문의해주세요")
       
bot.run(token)
