import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup    

class Corona(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def 코로나현황(self, ctx):
        try:
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
         except Exception as e:
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
            coembed.set_footer(text="질병관리본부에서 가져올수없었습니다.")
            await waitinfo.edit(embed = coembed)


def setup(bot):
    bot.add_cog(Corona(bot))
