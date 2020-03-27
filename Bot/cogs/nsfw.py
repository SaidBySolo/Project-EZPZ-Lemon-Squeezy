import discord
from discord.ext import commands
import requests
import asyncio
from bs4 import BeautifulSoup  
from .etc.botembed import BotEmbed  

class NSFW(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def 히요비번호(self, ctx, index):
        try:
            index = int(index)
        except ValueError:
            await ctx.send("숫자를 입력해주세요")
            return
        waitinfo = await ctx.send(embed = BotEmbed.waitinfoembed)
        URL = f'https://api.hiyobi.me/gallery/{index}'
        response = requests.get(URL).json()
        title = response['title']
        hiyoid = response['id']
        artist = [a['display'] for a in response['artists']]
        group = [g['display'] for g in response['groups']]
        parodys = [p['display'] for p in response['parodys']]
        characters = [c['display'] for c in response['characters']]
        tags = [t['display'] for t in response['tags']]
        if not artist:
            artist.append('없음')
        if not group:
            group.append('없음')
        if not parodys:
            parodys.append('없음')
        if not characters:
            characters.append('없음')
        if not tags:
            tags.append('없음')
        if any(title):
            embed = discord.Embed(title = title, url=f'https://hiyobi.me/reader/{hiyoid}')
            embed.set_thumbnail(url=f'https://cdn.hiyobi.me/tn/{hiyoid}.jpg')
            embed.add_field(name="작가", value=",".join(artist),  inline=False)
            embed.add_field(name="그룹", value=",".join(group),  inline=False)
            embed.add_field(name="원작", value=",".join(parodys),  inline=False)
            embed.add_field(name="캐릭터", value=",".join(characters),  inline=False)
            embed.add_field(name="태그", value=",".join(tags),  inline=False)
            await waitinfo.edit(embed = embed)
        else:
            embed = discord.Embed(title = "검색결과가 없는거같아요",description ="다시확인해주세요")
            await waitinfo.edit(embed = embed)

    @commands.command()
    async def 히요비검색(self, ctx, *tag):
        try:
            waitinfo = await ctx.send(embed = BotEmbed.waitinfoembed)
            search = [t for t in tag]
            data = {"search":search,"paging":1}
            URL = 'https://api.hiyobi.me/search'
            response = requests.post(URL, data=data).json()
            idlist = [a['id'] for a in response['list']]
            titlelist = [a['title'] for a in response['list']]
            artistslist = [a['artists'] for a in response['list']]
            grouplist = [g['groups'] for g in response['list']]
            parodyslist = [p['parodys'] for p in response['list']]
            characterslist = [c['characters'] for c in response['list']]
            tagslist = [t['tags'] for t in response['list']]
            hiyolist = [str(index) + ". " + t for index, t in enumerate(titlelist, 1)]
            if any(titlelist):
                embed = discord.Embed(title = "검색된 정보입니다.", description ="\n".join(hiyolist))
                await waitinfo.edit(embed = embed)
                await waitinfo.add_reaction("🔍")
                channel = ctx.channel
                def check(reaction, user):
                    return user == ctx.author and str(reaction.emoji) == '🔍'
                reaction, user = await self.bot.wait_for('reaction_add', check=check, timeout=300)
                def check2(m):
                    return m.channel == channel
                await ctx.send("30초이내에 번호를 입력하세요", delete_after=5)
                try:
                    response = await self.bot.wait_for('message', check=check2, timeout=30)
                except asyncio.TimeoutError:
                    await ctx.send("시간 초과입니다.")
                else:
                    if ctx.author == response.author:
                        fetmsg = await ctx.fetch_message(response.id)
                    title = titlelist[int(fetmsg.content) - 1]
                    hiyoid = idlist[int(fetmsg.content) - 1]
                    artist = [a['display'] for a in artistslist[int(fetmsg.content) - 1]]
                    group = [a['display'] for a in grouplist[int(fetmsg.content) - 1]]
                    parodys = [a['display'] for a in parodyslist[int(fetmsg.content) - 1]]
                    characters = [a['display'] for a in characterslist[int(fetmsg.content) - 1]]
                    tags = [a['display'] for a in tagslist[int(fetmsg.content) - 1]]
                    if not artist:
                        artist.append('없음')
                    if not group:
                        group.append('없음')
                    if not parodys:
                        parodys.append('없음')
                    if not characters:
                        characters.append('없음')
                    if not tags:
                        tags.append('없음')
                    embed = discord.Embed(title = title, url = f'https://hiyobi.me/reader/{hiyoid}')
                    embed.set_thumbnail(url=f'https://cdn.hiyobi.me/tn/{hiyoid}.jpg')
                    embed.add_field(name="작가", value=",".join(artist),  inline=False)
                    embed.add_field(name="그룹", value=",".join(group),  inline=False)
                    embed.add_field(name="원작", value=",".join(parodys),  inline=False)
                    embed.add_field(name="캐릭터", value=",".join(characters),  inline=False)
                    embed.add_field(name="태그", value=",".join(tags),  inline=False)
                    await fetmsg.delete()
                    await waitinfo.clear_reaction("🔍")
                    await waitinfo.edit(embed = embed)
            else:
                embed = discord.Embed(title = "검색결과가 없는거같아요",description ="다시확인해주세요")
                await waitinfo.edit(embed = embed)
                await waitinfo.clear_reaction("🔍")
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
        try:
            waitinfo = await ctx.send(embed = BotEmbed.waitinfoembed)
            URL = f'https://api.hiyobi.me/list/{num}'
            response = requests.get(URL).json()
            titlelist = [a['title'] for a in response['list']]
            idlist = [a['id'] for a in response['list']]
            artistslist = [a['artists'] for a in response['list']]
            grouplist = [g['groups'] for g in response['list']]
            parodyslist = [p['parodys'] for p in response['list']]
            characterslist = [c['characters'] for c in response['list']]
            tagslist = [t['tags'] for t in response['list']]
            hiyolist = [str(index) + ". " + t for index, t in enumerate(titlelist, 1)]
            if any(titlelist):
                embed = discord.Embed(title = "검색된 정보입니다.", description ="\n".join(hiyolist))
                await waitinfo.edit(embed = embed)
                await waitinfo.add_reaction("🔍")
                channel = ctx.channel
                def check(reaction, user):
                    return user == ctx.author and str(reaction.emoji) == '🔍'
                reaction, user = await self.bot.wait_for('reaction_add', check=check, timeout=300)
                def check2(m):
                    return m.channel == channel 
                await ctx.send("30초이내에 번호를 입력하세요", delete_after=5)
                try:
                    response = await self.bot.wait_for('message', check=check2, timeout=30)
                except asyncio.TimeoutError:
                    await ctx.send("시간 초과입니다.")
                else:
                    if ctx.author == response.author:
                        fetmsg = await ctx.fetch_message(response.id)
                    title = titlelist[int(fetmsg.content) - 1]
                    hiyoid = idlist[int(fetmsg.content) - 1]
                    artist = [a['display'] for a in artistslist[int(fetmsg.content) - 1]]
                    group = [a['display'] for a in grouplist[int(fetmsg.content) - 1]]
                    parodys = [a['display'] for a in parodyslist[int(fetmsg.content) - 1]]
                    characters = [a['display'] for a in characterslist[int(fetmsg.content) - 1]]
                    tags = [a['display'] for a in tagslist[int(fetmsg.content) - 1]]
                    if not artist:
                        artist.append('없음')
                    if not group:
                        group.append('없음')
                    if not parodys:
                        parodys.append('없음')
                    if not characters:
                        characters.append('없음')
                    if not tags:
                        tags.append('없음')
                    embed = discord.Embed(title = title, url = f'https://hiyobi.me/reader/{hiyoid}')
                    embed.set_thumbnail(url=f'https://cdn.hiyobi.me/tn/{hiyoid}.jpg')
                    embed.add_field(name="작가", value=",".join(artist),  inline=False)
                    embed.add_field(name="그룹", value=",".join(group),  inline=False)
                    embed.add_field(name="원작", value=",".join(parodys),  inline=False)
                    embed.add_field(name="캐릭터", value=",".join(characters),  inline=False)
                    embed.add_field(name="태그", value=",".join(tags),  inline=False)
                    await fetmsg.delete()
                    await waitinfo.clear_reaction("🔍")
                    await waitinfo.edit(embed = embed)
            else:
                embed = discord.Embed(title = "검색결과가 없는거같아요",description ="다시확인해주세요")
                await waitinfo.edit(embed = embed)
                await waitinfo.clear_reaction("🔍")      
        except Exception as e:
            embed = discord.Embed(title = "오류가발생한거같아요..:(", description = e)
            embed.set_footer(text="다시 시도해보시고 지속될경우 봇에게DM 또는 개인적으로 컨택해주세요.")
            await waitinfo.edit(embed = embed)

            
def setup(bot):
    bot.add_cog(NSFW(bot))
