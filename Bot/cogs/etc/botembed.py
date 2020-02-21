import discord
from discord.ext import commands
    
class BotEmbed:
       
    #help embed setting
    Helps = discord.Embed(title="Bot", color=0xffff80)
    Helps.set_author(name="Project EZPZ Lemon Squeezy", icon_url="https://imgur.com/j0yodUO.png")
    Helps.set_thumbnail(url="https://imgur.com/ysG49Sc.png")
    Helps.add_field(name="봇 이름", value="Martini", inline=False)
    Helps.add_field(name="접두사", value="?", inline=False)
    Helps.add_field(name="도움말", value="도움말창을 보여줍니다.", inline=False)
    Helps.add_field(name="내정보", value="자신의 디스코드 정보를 보여줍니다.", inline=False)
    Helps.add_field(name="주사위", value="기본값은 6이며, 숫자를 임의로 정할수있습니다.", inline=False)
    Helps.add_field(name="핑", value="봇의 응답시간을 보여줍니다 미국리전으로 평균적으로 45ms정도입니다.", inline=False)
    Helps.add_field(name="투표", value="투표기능입니다. 자세한건 +투표를 사용해주세요", inline=False)
    Helps.add_field(name="nsdw기능관련", value="이기능은 제한되어있습니다.", inline=False)
    Helps.add_field(name="연락처", value="SaidBySolo : 라고솔로가말했습니다#1234", inline=False)
    Helps.set_footer(text="ver 1.0.1 제작 - Sabin,SaidBySolo")


    #dev embed setting
    Dev = discord.Embed(title="개발진", color=0xffff80)
    Dev.set_author(name="Project EZPZ Lemon Squeezy", icon_url="https://imgur.com/j0yodUO.png")
    Dev.set_thumbnail(url="https://imgur.com/ysG49Sc.png")
    Dev.add_field(name="봇 이름", value="Martini", inline=False)
    Dev.add_field(name="메인개발진", value="Main Developer : Sabin, SaidBySolo ", inline=False)
    Dev.add_field(name="개발진", value="Developer : 김동규", inline=False)
    Dev.add_field(name="설명", value="2019년 12월 21일에 처음 커밋됬으며,\n현재는 비공개 리포지토리임", inline=False)
    Dev.set_footer(text="ver 1.0.1")

    
    

