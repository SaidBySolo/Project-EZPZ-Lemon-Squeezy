import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup    

class NSFW(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def 히요비넘버(self, ctx, index):
        try:
            index = int(index)
        except ValueError:
            await ctx.send("숫자를 입력해주세요")
            return

        response = requests.get('https://hiyobi.me/info/{}'.format(index))
        infohtml = response.text
        soup = BeautifulSoup(infohtml, 'lxml')
        table = soup.find('table')
        trs = table.find_all('tr')
        for title in soup.select('b'):
            nsfwtitle = title.text
            if len(soup.findAll('tr')) == 5:
                tags = [t.text for t in trs[:5]]
                nsfwser = discord.Embed(color=0x569271, title=nsfwtitle, description = "\n".join(tags))
                await ctx.send(embed = nsfwser)
            elif len(soup.findAll('tr')) == 4:
                tags = [t.text for t in trs[:4]]
                nsfwser = discord.Embed(color=0x569271, title=nsfwtitle, description = "\n".join(tags))
                await ctx.send(embed = nsfwser)
            elif len(soup.findAll('tr')) == 3:
                tags = [t.text for t in trs[:3]]
                nsfwser = discord.Embed(color=0x569271, title=nsfwtitle, description = "\n".join(tags))
                await ctx.send(embed = nsfwser)
            elif len(soup.findAll('tr')) == 2:
                tags = [t.text for t in trs[:2]]
                nsfwser = discord.Embed(color=0x569271, title=nsfwtitle, description = "\n".join(tags))
                await ctx.send(embed = nsfwser)
            
def setup(bot):
    bot.add_cog(NSFW(bot))