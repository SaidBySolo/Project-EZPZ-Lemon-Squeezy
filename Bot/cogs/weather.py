import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup
from .etc.botembed import BotEmbed

class Weather(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def 날씨(self, ctx, *, location):
        waitinfo = await ctx.send(embed = BotEmbed.waitinfoembed)
        response = requests.get(f'https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query={location}+날씨')
        readerhtml = response.text
        soup = BeautifulSoup(readerhtml, 'lxml')
        #===========================================
        nowtemp = soup.find('p', class_='info_temperature').find('span', class_='todaytemp').text
        infolo = soup.find('span', class_='btn_select').find('em').text
        #===========================================
        data1 = soup.find('div', class_='info_data')
        data2 = data1.findAll('li')
        cast = data2[0].find('p', class_='cast_txt').text
        mintemp = soup.find('span', class_='min').find('span', class_= 'num').text
        maxtemp = soup.find('span', class_='max').find('span', class_= 'num').text
        feeltemp = soup.find('span', class_='sensible').find('em').find('span', class_='num').text
        sunrainfo = data2[2].find('').find(text=True, recursive=False)
        sunranum = data2[2].find('span', class_='num').text
        sunranuminfo = data2[2].find(text=True, recursive=False)
        #===========================================
        data2 = soup.find('div', class_='detail_box')
        data3 = data2.findAll('dd')
        smalldust = data3[0].find('span', class_='num').text
        smalldustinfo = data3[0].find(text=True, recursive=False)
        verysmalldust = data3[1].find('span',class_='num').text
        verysmalldustinfo = data3[1].find(text=True, recursive=False)
        ozon = data3[2].find('span',class_='num').text
        ozoninfo = data3[2].find(text=True, recursive=False)
        #=============================================
        wem = discord.Embed(color=0x262131, title='날씨', description = f'{infolo}의 현재날씨입니다.' )
        wem.add_field(name="현재온도", value=f'{nowtemp}℃', inline=False)
        wem.add_field(name="날씨", value=f'{cast}', inline=False)
        wem.add_field(name="최저/최고", value=f'{mintemp}℃/{maxtemp}℃', inline=False)
        wem.add_field(name="체감온도", value=f'{feeltemp}℃', inline=False)
        wem.add_field(name=sunrainfo, value=f'{sunranum}  {sunranuminfo}', inline=False)
        wem.add_field(name="미세먼지", value=f'{smalldust}  {smalldustinfo}', inline=True)
        wem.add_field(name="초미세먼지", value=f'{verysmalldust}  {verysmalldustinfo}', inline=True)
        wem.add_field(name="오존지수", value=f'{ozon}  {ozoninfo}', inline=True)
        await waitinfo.edit(embed = wem)
        
def setup(bot):
    bot.add_cog(Weather(bot))