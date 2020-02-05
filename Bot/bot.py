import discord
import datetime
import random
import BotEmbed
import userdict
import asyncio
import requests
import json
from discord.ext import commands

#prefix
bot = commands.Bot(command_prefix='!')

#remove defalt help command
bot.remove_command ('help')

#paste token
token = "NjU3NjA0NDA3MDIxNjY2MzA0.Xf-JVw.Krgxt54ycfRKhRs0oQ5vSf7PLwI"

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
    
#commands
@bot.command()
async def 도움말(ctx):
    await ctx.send(embed = BotEmbed.Helps)

@bot.command()
async def passtravisbuild(ctx):
    print("Hello,World!")

@bot.command()
async def 제작현황(ctx):
    await ctx.send("제작중")

@bot.command()
async def ping(ctx):
    await ctx.send(":ping_pong:Pong! {0}".format(round(bot.latency, 1)))

@bot.command()
async def 핑(ctx):
    await ctx.send(":ping_pong:퐁! {0}".format(round(bot.latency, 1)))

#급식
async def 급식(ctx):
    await ctx.send("오늘의 급식입니다.")

@bot.command()
async def 투표(ctx):
    message = await ctx.send(embed=BotEmbed.Vote1)
    for emoji in ('✅', '❎'):
        await message.add_reaction(emoji)

    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) == '✅' or user == ctx.author and str(reaction.emoji) == '❎'

    try:
        reaction, user = await bot.wait_for('reaction_add', timeout=10.0, check=check)
    except asyncio.TimeoutError:
        await message.edit(embed = BotEmbed.TimeOut)
    else:
        if str(reaction.emoji) == '✅':
            message2 = await message.edit(embed=BotEmbed.Vote2)
        else:
            await message.edit(embed = BotEmbed.Cancle)
  

#Information command
@bot.command()
async def 내정보(ctx):
    react_embed = userdict.user_embed.get(ctx.author.id)
    if react_embed is not None: 
        await ctx.send(embed = react_embed)
    else:
        await ctx.send("엠베드가 존재하지않슴니다. 관리자에게 문의해주세요")
       

#급식parser
now = datetime.datetime.now()
year = str(now.year)
month = str(now.month)
date = str(now.day)
#인천남고
@bot.command()
async def 인남급식(ctx):
    innamUrl = 'https://schoolmenukr.ml/api/middle/E100000262?year=' + year + '&month=' + month + '&date=' + date + '&hideAllergy=true'
    innamResponse = requests.get(innamUrl)
    innam_school_menu = json.loads(innamResponse.text)
    await ctx.send(innam_school_menu)

@bot.command()
async def 인기공급식(ctx):
    ingiUrl = 'https://schoolmenukr.ml/api/middle/E100000261?year=' + year + '&month=' + month + '&date=' + date + '&hideAllergy=true'
    ingiResponse = requests.get(ingiUrl)
    ingi_school_menu = json.loads(ingiResponse.text)
    await ctx.send(ingi_school_menu)

@bot.command()
async def 인고급식(ctx):
    incheonUrl = 'https://schoolmenukr.ml/api/middle/E100000258?year=' + year + '&month=' + month + '&date=' + date + '&hideAllergy=true'
    incheonResponse = requests.get(incheonUrl)
    incheon_school_menu = json.loads(incheonResponse.text)
    await ctx.send(incheon_school_menu)

bot.run(token)
