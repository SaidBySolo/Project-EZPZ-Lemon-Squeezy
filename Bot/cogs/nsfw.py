import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup  
from .etc.botembed import BotEmbed  

class NSFW(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    @commands.is_nsfw() 
    async def 히요비넘버(self, ctx, index):
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
        
    @commands.command()
    async def 히요비리스트(self, ctx, num):
        response = requests.get(f"https://hiyobi.me/list/{num}")
        readerhtml = response.text
        soup = BeautifulSoup(readerhtml, 'lxml')
        soup.findAll('div', class_='gallery-content row')

            
def setup(bot):
    bot.add_cog(NSFW(bot))