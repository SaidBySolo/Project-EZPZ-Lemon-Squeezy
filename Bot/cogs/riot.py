import discord
from discord.ext import commands
from riotwatcher import LolWatcher
import json
from .etc.ranks import ranks
from .etc.botembed import BotEmbed

with open("Bot/cogs/etc/Auth.json", "r") as riottoken:
    token = json.load(riottoken)

region = "kr"
watcher = LolWatcher(token['riottoken'])

class Riot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="롤")
    async def lolinfo(self, ctx, *, user):
        waitinfo = await ctx.send(embed = BotEmbed.waitinfoembed)
        try:
            summonerinfo = watcher.summoner.by_name(region, user)
        except Exception:
            nouserembed = discord.Embed(title=f"존재하지않는 유저인거같아요",description="확인후 다시시도 해주세요")
            await waitinfo.edit(embed=nouserembed)
        summonername = summonerinfo['name']
        summonerid = summonerinfo['id']
        summonerenid = summonerinfo['accountId']
        summonerlv = summonerinfo['summonerLevel']

        summonerranks = watcher.league.by_summoner(region, summonerid)
        if not summonerranks:
            nsrembed = discord.Embed(title=f"{summonername}님의 솔로랭크 정보가 없는거 같아요...",description="확인후 다시시도 해주세요")
            await waitinfo.edit(embed=nsrembed)
        elif len(summonerranks) == 2:
            summonerranks = summonerranks[0]
        else:
            summonerranks = summonerranks[0]

        queuetype = ranks.rankdict[summonerranks['queueType']]
        tear = ranks.rankdict[summonerranks['tier']]
        rank = ranks.rankdict[summonerranks['rank']]
        point = summonerranks['leaguePoints']
        win = summonerranks['wins']
        loss = summonerranks['losses']
        #embed
        embed = discord.Embed(title=f"{summonername}님의 검색 결과입니다.", description=f"{queuetype}")
        embed.set_thumbnail(url=ranks.rankdict[f'{tear}img'])
        embed.add_field(name="레벨", value=f"{summonerlv}레벨", inline=True)
        embed.add_field(name=f"{tear} {rank}", value=f"{point}LP", inline=True)
        embed.add_field(name="승/패", value=f"{win}승/{loss}패", inline=True)
        embed.add_field(name="승률", value=f"{round(win/(win+loss)*100, 2)}%",inline=True)
        await waitinfo.edit(embed=embed)
        

def setup(bot):
    bot.add_cog(Riot(bot))