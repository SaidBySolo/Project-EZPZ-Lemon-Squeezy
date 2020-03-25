from pixivpy3 import *
import os
import discord
from discord.ext import commands
from .etc.botembed import BotEmbed
import json

with open(os.path.abspath("Bot/cogs/etc/Auth.json"), "r") as PixLogin:
    Auth = json.load(PixLogin)

def Login():
    aapi = AppPixivAPI()
    aapi.login(Auth["_username"], Auth["_password"])
    return aapi

class Pixiv(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def 픽시브번호(self, ctx, num):
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
    async def 픽시브랭킹(self, ctx):
        await ctx.send("개발중", delete_after=5)

def setup(bot):
    bot.add_cog(Pixiv(bot))