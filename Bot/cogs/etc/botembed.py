import datetime
import discord
from discord.ext import commands
    

class BotEmbed:
       
    #help embed setting
    Helps = discord.Embed(title="Bot", color=0xffff80)
    Helps.set_author(name="EZPZ Lemon Squeezy", icon_url="https://imgur.com/j0yodUO.png")
    Helps.set_thumbnail(url="https://imgur.com/ysG49Sc.png")
    Helps.add_field(name="봇 이름", value="???", inline=False)
    Helps.add_field(name="메인개발진", value="Main Developer : Sabin, SaidBySolo ", inline=False)
    Helps.add_field(name="개발진", value="Developer : 김동규", inline=False)
    Helps.add_field(name="명령어", value="!도움말 : 도움말을 보여줍니다.\n안녕 : 인사해줍니다. 착해요.\n!제작현황 : 제작 현황이 나옵니다. 근데 쓸데없어요.\n!내정보 : 자신의 프로필이 나옵니다. 업데이트는 느려요.", inline=False)
    Helps.add_field(name="연락처", value="Sabin : Sabin#9478 (많이 연락하지 마세요....)\nSaidBySolo : 라고솔로가말했습니다#1234", inline=False)
    Helps.set_footer(text="ver 1.0.1    제작 - Sabin")
    

