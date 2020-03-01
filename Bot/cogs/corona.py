import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup    

class Corona(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def 코로나현황(self, ctx):
        waitinfoembed = discord.Embed(title="서버로부터 가져오는중이에요!", description = "잠시만기다려주세요..")
        waitinfo = await ctx.send(embed = waitinfoembed)
        response = requests.get('http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=&brdGubun=&ncvContSeq=&contSeq=&board_id=&gubun=')
        readerhtml = response.text
        soup = BeautifulSoup(readerhtml, 'lxml')
        bigclass = soup.find('div', class_='bv_content')
        nowtitle = bigclass.find('p', class_='s_descript').text
        allinfokr = bigclass.find('tbody').findAll('td')
        #===============================
        coembed = discord.Embed(color=0x192131, title='코로나현황', description =f'{nowtitle}' )
        coembed.add_field(name="확진자", value=f'{allinfokr[0].text}', inline=True)
        coembed.add_field(name="확진자 격리해제", value=f'{allinfokr[1].text}', inline=True)
        coembed.add_field(name="검사중", value=f'{allinfokr[3].text}', inline=True)
        coembed.add_field(name="사망자", value=f'{allinfokr[2].text}', inline=True)
        await waitinfo.edit(embed = coembed)


def setup(bot):
    bot.add_cog(Corona(bot))