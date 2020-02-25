import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup    

class Corona(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def 코로나현황(self, ctx):
        response = requests.get('https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=코로나')
        readerhtml = response.text
        soup = BeautifulSoup(readerhtml, 'lxml')
        data1 = soup.find('div', class_='graph_view')
        data2 = data1.findAll('div', class_='box')
        data3 = data1.findAll('div', class_='box bottom')
        checked = data2[0].find('p', class_='txt').find('strong', class_='num').text
        checking = data2[2].find('p', class_='txt').find('strong', class_='num').text
        free = data3[0].find('p', class_='txt').find('strong', class_='num').text        
        die = data3[1].find('p', class_='txt').find('strong', class_='num').text
        wasup = soup.find('div', class_='csp_notice_info').find('p').find_all(text=True, recursive=True)
        #===============================
        coembed = discord.Embed(color=0x192131, title='코로나현황', description =f'{wasup[1]}' )
        coembed.add_field(name="확진자", value=f'{checked}명', inline=True)
        coembed.add_field(name="격리해제", value=f'{free}명', inline=True)
        coembed.add_field(name="검사중", value=f'{checking}명', inline=True)
        coembed.add_field(name="사망자", value=f'{die}명', inline=True)
        await ctx.send(embed = coembed)

def setup(bot):
    bot.add_cog(Corona(bot))