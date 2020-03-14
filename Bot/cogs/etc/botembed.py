import discord
from discord.ext import commands
    
class BotEmbed:
       
    #help embed setting
    Helps = discord.Embed(title="도움말", color=0xffff80)
    Helps.set_author(name="Project EZPZ Lemon Squeezy", icon_url="https://imgur.com/j0yodUO.png")
    Helps.set_thumbnail(url="https://imgur.com/ysG49Sc.png")
    Helps.add_field(name="접두사", value="&", inline=False)
    Helps.add_field(name="사용법", value="&도움말 (페이지) ex.&도움말 1")


    Helps1 = discord.Embed(title="도움말 1번째페이지", color=0xffff80)
    Helps1.add_field(name="문의", value="문의방법을 설명해드립니다.", inline=False)
    Helps1.add_field(name="도움말", value="총 3페이지까지있습니다.", inline=False)
    Helps1.add_field(name="내정보", value="자신의 디스코드 정보를 보여줍니다.", inline=False)
    Helps1.add_field(name="주사위", value="기본값은 6이며, 숫자를 임의로 정할수있습니다.", inline=False)
    Helps1.add_field(name="핑", value="봇의 응답시간을 보여줍니다 미국리전으로 평균적으로 45ms정도입니다.", inline=False)
    Helps1.add_field(name="투표", value="투표기능입니다. 자세한건 &투표를 사용해주세요", inline=False)
    Helps1.add_field(name="링크", value="봇초대링크를 가져옵니다.\n해당링크는 권한 최적화를 해두지않았으므로 초대하실때 참고하시길바랍니다.", inline=False)

    Helps2 = discord.Embed(title="도움말 2번째페이지", color=0xffff80)
    Helps2.add_field(name="connect", value="음성채널 접속", inline=False) 
    Helps2.add_field(name="play", value="노래 재생", inline=False)  
    Helps2.add_field(name="stop", value="재생중인 노래를 전부멈추고 음성채널을 나갑니다.", inline=False)   
    Helps2.add_field(name="queue", value="노래 대기열", inline=False)  
    Helps2.add_field(name="np", value="재생중인 노래", inline=False)
    Helps2.add_field(name="pause", value="재생중인 노래를 일시중지합니다.", inline=False)    
    Helps2.add_field(name="resume", value="일시중지한 노래를 재생합니다.", inline=False)
    
    Helps3 = discord.Embed(title="도움말 3번째페이지", color=0xffff80)
    Helps3.add_field(name="코로나현황", value="질병관리본부에서 코로나 확진자등 정보를 가져옵니다.\n가져올수없을경우 네이버에서가져옵니다.", inline=False)
    Helps3.add_field(name="픽시브번호", value="픽시브 그림의 번호를주시면 원본화질로 가져옵니다.")  
    Helps3.add_field(name="히요비관련 명령어",value="히요비관련 명령어는 nsfw채널에서만 사용하실수있습니다.")
    Helps3.add_field(name="히요비검색", value="태그또는제목으로 검색하실수있습니다.\n단일태그 검색예시:&히요비검색 type:manga\n복수태그 검색예시:&히요비검색 type:manga|female:big_breasts", inline=False)
    Helps3.add_field(name="히요비번호", value="히요비번호를 주시면 해당 만화의 상세정보를보여줍니다.", inline=False)
    Helps3.add_field(name="히요비리스트", value="리스트번호를 주시면 해당리스트의 모든 만화를보여줍니다.\n최신으로 올라온것을 확인하시려면 1을 인자값으로 주시면됩니디.", inline=False)
    Helps3.add_field(name="날씨", value="현재 날씨를 네이버에서 크롤링 하여 가져옵니다.\n예시:&날씨 인천\n상세위치예시:&날씨 인천 남동구", inline=False)          


    #wait info
    waitinfoembed = discord.Embed(title="서버로부터 가져오는중이에요!", description = "잠시만기다려주세요.....")
    waitinfoembed.set_footer(text="이 메세지가 계속뜨고 지속된다면 명령어를 맞게,없는정보를 요청하였는지확인하고\n 그래도 이문제가 계속될경우 봇에게 DM해주세요.")

    #dev embed setting
    Dev = discord.Embed(title="개발진", color=0xffff80)
    Dev.set_author(name="Project EZPZ Lemon Squeezy", icon_url="https://imgur.com/j0yodUO.png")
    Dev.set_thumbnail(url="https://imgur.com/ysG49Sc.png")
    Dev.add_field(name="봇 이름", value="Martini", inline=False)
    Dev.add_field(name="메인개발진", value="Main Developer : Sabin, SaidBySolo ", inline=False)
    Dev.add_field(name="개발진", value="Developer : 김동규", inline=False)
    Dev.add_field(name="설명", value="2019년 12월 21일에 처음 커밋됬으며,\n현재는 비공개 리포지토리임", inline=False)
    Dev.set_footer(text="ver 1.1.1")

    
    

