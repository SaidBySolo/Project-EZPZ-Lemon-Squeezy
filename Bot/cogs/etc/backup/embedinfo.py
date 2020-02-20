import discord
from discord.ext import commands
import datetime

#time
now = datetime.datetime.now()

#Sabin Embed setting
Sabin = discord.Embed(title="Sabin", description="This Embed is a Profile of Sabin", color=0x569271)
Sabin.set_author(name="Name : ")
Sabin.set_thumbnail(url="https://imgur.com/Kv17Jnm.gif")
Sabin.add_field(name="Position", value="Leader Developer", inline=False)
Sabin.add_field(name="Status", value=":tired_face:", inline=False)
Sabin.add_field(name="Contact Information",value="Discord : Sabin#9478", inline=False)
Sabin.set_footer(text="Don't call me...." + str(now.year) + "년 " + str(now.month) + "월 " + str(now.day) + "일 | " + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second))

#SaidBySolo Embed setting
SaidBySolo = discord.Embed(title="SaidBySolo", description="This Embed is a Profile of SaidBySolo", color=0x569271)
SaidBySolo.set_author(name="Name : ")
SaidBySolo.set_thumbnail(url="https://imgur.com/YBZEvFq.png")
SaidBySolo.add_field(name="Position", value="Leader Developer", inline=False)
SaidBySolo.add_field(name="Status", value=":thinking:", inline=False)
SaidBySolo.add_field(name="Contact Information",value="Discord : 라고솔로가말했습니다#1234", inline=False)
SaidBySolo.set_footer(text="SaidBySolo " + str(now.year) + "년 " + str(now.month) + "월 " + str(now.day) + "일 | " + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second))

#Bliz Embed setting
Bliz = discord.Embed(
    title="Bliz", description="This Embed is a Profile of bliz", color=0x569271)

#Unoh03 Embed setting
Unoh03 = discord.Embed(title="Unoh03", description="This Embed is a Profile of Unoh03", color=0x569271)
Unoh03.set_author(name="Name : ")
Unoh03.set_thumbnail(url="https://imgur.com/wEDioHB.png")
Unoh03.add_field(name="Position", value="Tester", inline=False)
Unoh03.add_field(name="Status", value=":angry:", inline=False)
Unoh03.add_field(name="Contact Information",value="Discord : Unoh03#6944", inline=False)
Unoh03.set_footer(text="I'm not a developer!!" + str(now.year) + "년 " + str(now.month) +"월 " + str(now.day) + "일 | " + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second))

#Dong9 Embed setting
Dong9 = discord.Embed(
    title="Dong9", description="This Embed is a Profile of Dong9", color=0x569271)
Dong9.set_author(name="Name :")
Dong9.set_thumbnail(url="https://imgur.com/HEMbhcj.gif")
Dong9.add_field(name="Position", value="Developer", inline=False)
Dong9.add_field(name="Status", value=":zipper_mouth:", inline=False)
Dong9.add_field(name="Contact Information",value="Discord : 김동규#0285", inline=False)
Dong9.set_footer(text="." + str(now.year) + "년 " + str(now.month) + "월 " + str(now.day) + "일 | " + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second))

#Decfcone1 Embed setting
Decfcone1 = discord.Embed(title="Decfcone1", description="This Embed is a Profile of Decfcone1", color=0x569271)

#JH Embed setting
JH = discord.Embed(title="JH", description="This Embed is a Profile of JH", color=0x569271)

#Huggy Embed setting
Huggy = discord.Embed(title="Huggy", description="This Embed is a Profile of Huggy", color=0x569271)

#Cancle Embed setting
Cancle = discord.Embed(title="취소 되었습니다.", color=0xfc2210)

#TimeOut bed setting
TimeOut = discord.Embed(title="시간 초과 입니다 다시 시도해주세요", color=0xfc2210)

#Vote1 Embed setting
Vote1 = discord.Embed(title="투표를 생성하시겠습니까?",description="생성자:", color=0x569271)
Vote1.add_field(name="이모지에 반응하여주세요",value=" :white_check_mark:생성\n:negative_squared_cross_mark:생성취소", inline=False)
Vote1.set_footer(text="생성일시:" + str(now.year) + "년 " + str(now.month) + "월 " + str(now.day) + "일" + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second))

#Vote2 Embed setting
Vote2 = discord.Embed(title="제목을 입력해주세요.",description="생성자:", color=0x569271)
Vote2.set_footer(text="생성일시:" + str(now.year) + "년 " + str(now.month) + "월 " + str(now.day) + "일" + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second))


async def 내정보(self, ctx):
    react_embed = UserDict.user_embed.get(ctx.author.id)
    if react_embed is not None:
        await ctx.send(embed=react_embed)
    else:
        await ctx.send("엠베드가 존재하지않슴니다. 관리자에게 문의해주세요")
