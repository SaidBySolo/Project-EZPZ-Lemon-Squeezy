import requests
import json
from bs4 import BeautifulSoup
import datetime
import discord
from discord.ext import commands

#미완성.
now = datetime.datetime.now()
year = str(now.year)
month = str(now.month)
date = str(now.day)

class Lunch(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def 급식(self, ctx, scname):
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

def setup(bot):
    bot.add_cog(Lunch(bot))       