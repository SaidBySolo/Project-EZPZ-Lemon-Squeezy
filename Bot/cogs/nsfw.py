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
        soup = BeautifulSoup(infohtml, 'html.parser')
        for title in soup.select('b'):
            await ctx.send(title.text)
            for tag in soup.select('tr'):
                await ctx.send(tag.text)
                
def setup(bot):
    bot.add_cog(NSFW(bot))