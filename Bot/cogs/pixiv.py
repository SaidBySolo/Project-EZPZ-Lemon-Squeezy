from pixivpy3 import *
import discord
from discord.ext import commands
from .etc.botembed import BotEmbed
from .etc import Auth

def Login():
    aapi = AppPixivAPI()
    aapi.login(Auth._username, Auth._password)
    return aapi

class Pixiv(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def 픽시브검색(self, ctx, num):
        try:
            num = int(num)
        except ValueError:
            await ctx.send("숫자를 입력해주세요")
            return
        waitinfo = await ctx.send(embed = BotEmbed.waitinfoembed)
        json_result = Login().illust_detail(num)
        illust = json_result.illust
        pembed = discord.Embed(color=0x262131, title=illust.title, url=f'https://www.pixiv.net/en/artworks/{num}', description = illust.user.name)
        pembed.set_image(url=illust.image_urls.large.replace('https://i.pximg.net/c/600x1200_90_webp', 'https://tc-pximg01.techorus-cdn.com'))
        await waitinfo.edit(embed = pembed)                       
         
    @commands.command()
    @commands.is_nsfw()
    async def 픽시브태그(self, ctx, tag):
        waitinfo = await ctx.send(embed = BotEmbed.waitinfoembed)
        json_result = Login().search_illust(tag, search_target='partial_match_for_tags')
        illust = json_result.illusts[0]
        pembed = discord.Embed(color=0x262131, title=illust.title, url=f'https://www.pixiv.net/en/artworks/{illust.id}', description = illust.user.name)
        pembed.set_image(url=illust.image_urls.large.replace('https://i.pximg.net/c/600x1200_90_webp', 'https://tc-pximg01.techorus-cdn.com'))
        await waitinfo.edit(embed = pembed)


def setup(bot):
    bot.add_cog(Pixiv(bot))