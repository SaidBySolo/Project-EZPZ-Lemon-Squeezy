import requests
import json
from bs4 import BeautifulSoup
import datetime
import discord
from discord.ext import commands
from .etc.botembed import BotEmbed  

#기능구현완료.
now = datetime.datetime.now()
year = str(now.year)
month = str(now.month)
date = str(now.day)

class Lunch(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def 급식(self, ctx, scname):
        waitinfo = await ctx.send(embed = BotEmbed.waitinfoembed)
        response = requests.get(f'https://schoolmenukr.ml/code/app?q={scname}')
        readerhtml = response.text
        soup = BeautifulSoup(readerhtml, 'lxml')
        sccode = soup.find('div', class_='school-info').find('h3', class_='school-code').text
        if "초등학교" in ctx.message.content:
            scclass = "elementary"
        elif "중학교" in ctx.message.content:
            scclass = "middle"
        elif "고등학교" in ctx.message.content:
            scclass = "high"
        lunchinfo = f"https://schoolmenukr.ml/api/{scclass}/{sccode}?year={year}&month={month}&date={date}&hideAllergy=true"
        lunchResponse = requests.get(lunchinfo).json()  
        lunchdict = lunchResponse.get('menu')
        lunchchange = {**lunchdict[0]}
        lunch = list(lunchchange.get('lunch'))
        if any(lunch):
            lunchembed = discord.Embed(color=0x192771, title=f"{scname}의 오늘급식입니다", description = "\n".join(lunch))
            await waitinfo.edit(embed = lunchembed)
        else:
            nonlunch = discord.Embed(title="오늘 급식이 없는거같아요..")
            await waitinfo.edit(embed = nonlunch)
        
        
def setup(bot):
    bot.add_cog(Lunch(bot))       