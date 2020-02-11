import requests
import json
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
    
    #인천남고
    @commands.command()
    async def 인남급식(self,ctx):
        innamUrl = 'https://schoolmenukr.ml/api/middle/E100000262?year=' + year + '&month=' + month + '&date=' + date + '&hideAllergy=true'
        innamResponse = requests.get(innamUrl)
        innam_school_menu = json.loads(innamResponse.text)
        await ctx.send(innam_school_menu)

    #인천기계공업고등학교
    @commands.command()
    async def 인기공급식(self, ctx):
        ingiUrl = 'https://schoolmenukr.ml/api/middle/E100000261?year=' + year + '&month=' + month + '&date=' + date + '&hideAllergy=true'
        ingiResponse = requests.get(ingiUrl)
        ingi_school_menu = json.loads(ingiResponse.text)
        await ctx.send(ingi_school_menu)

    #인천고등학교
    @commands.command()
    async def 인고급식(self, ctx):
        incheonUrl = 'https://schoolmenukr.ml/api/middle/E100000258?year=' + year + '&month=' + month + '&date=' + date + '&hideAllergy=true'
        incheonResponse = requests.get(incheonUrl)
        incheon_school_menu = json.loads(incheonResponse.text)
        await ctx.send(incheon_school_menu)

def setup(bot):
    bot.add_cog(Lunch(bot))       