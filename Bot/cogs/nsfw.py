import discord
from discord.ext import commands
import requests
import asyncio
from bs4 import BeautifulSoup  
from .etc.botembed import BotEmbed  

class NSFW(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    #최적화 예정
    @commands.command()
    @commands.is_nsfw() 
    async def 히요비번호(self, ctx, index):
        try:
            index = int(index)
        except ValueError:
            await ctx.send("숫자를 입력해주세요")
            return
        waitinfo = await ctx.send(embed = BotEmbed.waitinfoembed)
        response = requests.get(f'https://hiyobi.me/info/{index}')
        readerhtml = response.text
        soup = BeautifulSoup(readerhtml, 'lxml')
        table = soup.find('table')
        trs = table.findAll('tr')
        for title in soup.select('b'):
            nsfwtitle = title.text
            if len(soup.findAll('tr')) == 5:
                tags = [t.text for t in trs[:5]]
                nsfwser = discord.Embed(color=0x569271, title=nsfwtitle, description = "\n".join(tags))
                nsfwser.add_field(name="링크", value=f'https://hiyobi.me/reader/{index}',  inline=False)
                nsfwser.set_thumbnail(url=f'https://hiyobi.me/tn/{index}.jpg')
                await waitinfo.edit(embed = nsfwser)
            elif len(soup.findAll('tr')) == 4:
                tags = [t.text for t in trs[:4]]
                nsfwser = discord.Embed(color=0x569271, title=nsfwtitle, description = "\n".join(tags))
                nsfwser.add_field(name="링크", value=f'https://hiyobi.me/reader/{index}',  inline=False)
                nsfwser.set_thumbnail(url=f'https://hiyobi.me/tn/{index}.jpg')
                await waitinfo.edit(embed = nsfwser)
            elif len(soup.findAll('tr')) == 3:
                tags = [t.text for t in trs[:3]]
                nsfwser = discord.Embed(color=0x569271, title=nsfwtitle, description = "\n".join(tags))
                nsfwser.add_field(name="링크", value=f'https://hiyobi.me/reader/{index}',  inline=False)
                nsfwser.set_thumbnail(url=f'https://hiyobi.me/tn/{index}.jpg')
                await waitinfo.edit(embed = nsfwser)
            elif len(soup.findAll('tr')) == 2:
                tags = [t.text for t in trs[:2]]
                nsfwser = discord.Embed(color=0x569271, title=nsfwtitle, description = "\n".join(tags))
                nsfwser.add_field(name="링크", value=f'https://hiyobi.me/reader/{index}',  inline=False)
                nsfwser.set_thumbnail(url=f'https://hiyobi.me/tn/{index}.jpg')
                await waitinfo.edit(embed = nsfwser)

    @commands.is_nsfw()
    @commands.command()
    async def 히요비검색(self, ctx, tag):
        try:
            waitinfo = await ctx.send(embed = BotEmbed.waitinfoembed)
            response = requests.get(f"https://hiyobi.me/search/{tag}")
            readerhtml = response.text
            soup = BeautifulSoup(readerhtml, 'lxml')
            bigresult = soup.findAll('div', class_='gallery-content row')
            titleall = soup.findAll('b')
            title = [str(index) +". " + t.text for index, t in enumerate(titleall, 1)]
            embed = discord.Embed(title = "검색된 정보입니다.", description ="\n".join(title))
            await waitinfo.edit(embed = embed)
            await waitinfo.add_reaction("🔍")
            channel = ctx.channel
            def check(reaction, user):
                return user == ctx.author and str(reaction.emoji) == '🔍'
            reaction, user = await self.bot.wait_for('reaction_add', check=check)
            def check2(m):
                return m.channel == channel 
            try:
                await ctx.send("30초이내에 번호를 입력하세요", delete_after=5)
                response = await self.bot.wait_for('message', check=check2, timeout=30)
            except asyncio.TimeoutError:
                await ctx.send("시간 초과입니다.")
            else:
                if ctx.author == response.author:
                    fetmsg = await ctx.fetch_message(response.id)
                smalltitle = bigresult[int(fetmsg.content) - 1].find('span')
                resulttitle = smalltitle.find('b').text 
                result = smalltitle.findAll('tr')   
                tags = [t.text for t in result]
                embed = discord.Embed(title = resulttitle, description ="\n".join(tags))
                await waitinfo.edit(embed = embed)
        except Exception as e:
            embed = discord.Embed(title = "오류가발생한거같아요..:(", description = e)
            embed.set_footer(text="다시 시도해보시고 지속될경우 봇에게DM 또는 개인적으로 컨택해주세요.")
            await waitinfo.edit(embed = embed)
        
    @commands.command()
    async def 히요비리스트(self, ctx, num):
        try:
            int(num)
        except ValueError:
            await ctx.send("정수로 입력해주세요", delete_after=5)
        else:
            try:
                waitinfo = await ctx.send(embed = BotEmbed.waitinfoembed)
                response = requests.get(f"https://hiyobi.me/list/{num}")
                readerhtml = response.text
                soup = BeautifulSoup(readerhtml, 'lxml')
                bigresult = soup.findAll('div', class_='gallery-content row')
                titleall = soup.findAll('b')
                title = [str(index) +". " + t.text for index, t in enumerate(titleall, 1)]
                embed = discord.Embed(title = "검색된 정보입니다.", description ="\n".join(title))
                await waitinfo.edit(embed = embed)
                await waitinfo.add_reaction("🔍")
                channel = ctx.channel
                def check(reaction, user):
                    return user == ctx.author and str(reaction.emoji) == '🔍'
                reaction, user = await self.bot.wait_for('reaction_add', check=check)
                def check2(m):
                    return m.channel == channel 
                try:
                    await ctx.send("30초이내에 번호를 입력하세요", delete_after=5)
                    response = await self.bot.wait_for('message', check=check2, timeout=30)
                except asyncio.TimeoutError:
                    await ctx.send("시간 초과입니다.")
                else:
                    if ctx.author == response.author:
                        fetmsg = await ctx.fetch_message(response.id)
                    smalltitle = bigresult[int(fetmsg.content) - 1].find('span')
                    resulttitle = smalltitle.find('b').text 
                    result = smalltitle.findAll('tr')   
                    tags = [t.text for t in result]
                    embed = discord.Embed(title = resulttitle, description ="\n".join(tags))
                    await waitinfo.edit(embed = embed)
            except Exception as e:
                embed = discord.Embed(title = "오류가발생한거같아요..:(", description = e)
                embed.set_footer(text="다시 시도해보시고 지속될경우 봇에게DM 또는 개인적으로 컨택해주세요.")
                await waitinfo.edit(embed = embed)

            
def setup(bot):
    bot.add_cog(NSFW(bot))