import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup    

class Weather(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def 날씨(self, ctx, *, location):
        response = requests.get(f'https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query={location}+날씨')
        readerhtml = response.text
        soup = BeautifulSoup(readerhtml, 'lxml')
        nowtemp = soup.find('p', class_='info_temperature').find('span', class_='todaytemp').text
        cast = soup.find('ul', class_='info_list').find('p', class_='cast_txt').text
        infolo = soup.find('span', class_='btn_select').find('em').text
        mintemp = soup.find('span', class_='min').find('span', class_= 'num').text
        maxtemp = soup.find('span', class_='max').find('span', class_= 'num').text
        feeltemp = soup.find('span', class_='sensible').find('em').find('span', class_='num').text
        sunnum = soup.find('span', class_='indicator').find('span', class_='num').text
        suninfo = soup.find('span', class_='indicator').find('').find(text=True, recursive=False)
        data1 = soup.find('div', class_='detail_box')
        data2 = data1.findAll('dd')
        smalldust = data2[0].find('span', class_='num').text
        smalldustinfo = data2[0].find(text=True, recursive=False)
        verysmalldust = data2[1].find('span',class_='num').text
        verysmalldustinfo = data2[1].find(text=True, recursive=False)
        ozon = data2[2].find('span',class_='num').text
        ozoninfo = data2[2].find(text=True, recursive=False)
        #=============================================
        wem = discord.Embed(color=0x262131, title='날씨', description = f'{infolo}의 현재날씨입니다.' )
        wem.add_field(name="현재온도", value=f'{nowtemp}℃', inline=False)
        wem.add_field(name="날씨", value=f'{cast}', inline=False)
        wem.add_field(name="최저/최고", value=f'{mintemp}℃/{maxtemp}℃', inline=False)
        wem.add_field(name="체감온도", value=f'{feeltemp}℃', inline=False)
        wem.add_field(name="자외선", value=f'{sunnum} | {suninfo}', inline=False)
        wem.add_field(name="미세먼지", value=f'{smalldust} | {smalldustinfo}', inline=True)
        wem.add_field(name="초미세먼지", value=f'{verysmalldust} | {verysmalldustinfo}', inline=True)
        wem.add_field(name="오존지수", value=f'{ozon} | {ozoninfo}', inline=True)
        await ctx.send(embed = wem)
        
def setup(bot):
    bot.add_cog(Weather(bot))