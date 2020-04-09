import discord
from discord.ext import commands
from riotwatcher import LolWatcher
import json
from .etc.ranks import ranks

with open("Bot/cogs/etc/Auth.json", "r") as riottoken:
    token = json.load(riottoken)

region = "kr"
watcher = LolWatcher(token['riottoken'])

class Riot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="롤")
    async def lolinfo(self, ctx, *, user):
        summonerinfo = watcher.summoner.by_name(region, user)
        summonername = summonerinfo['name']
        summonerid = summonerinfo['id']
        summonerenid = summonerinfo['accountId']
        summonerlv = summonerinfo['summonerLevel']

        summonerranks = watcher.league.by_summoner(region, summonerid)
        checksoloranks = len(summonerranks)
        if checksoloranks == 2:
            summonerranks = summonerranks[1]
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
        await ctx.send(embed=embed)
        

def setup(bot):
    bot.add_cog(Riot(bot))
