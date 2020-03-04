import discord
from discord.ext import commands
import datetime

class Notice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def 공지(self, ctx, setchannel):
        now = datetime.datetime.now()
        embed = discord.Embed(title="공지", description=f"Alpha 1.1.1 패치노트", color=0x218362)
        embed.add_field(name="급식기능추가", 
                        value="전국 초,중,고의 급식을 가져올수있으나...\n이번 코로나19 바이러스로 해당기능은 23일날 사용하실수있도록 하겠습니다.", 
                        inline=False)
        embed.add_field(name="픽시브관련", 
                        value="픽시브의 그림을 원본 화질로 만나보실수있습니다.\n픽시브 링크를 올릴시나오는 임베드의 그림은 잘려나오는등 미리보기에 힘들었습니다.\n해당 문제를보고 보완했습니다.", 
                        inline=False)
        embed.set_image(url="https://media.discordapp.net/attachments/657845095223132160/684593046918397955/unknown.png?width=304&height=475")
        embed.add_field(name="코로나현황 안정성", value="질병관리본부에서만 가져오고있었는데 질병관리본부 홈페이지가 응답을 하지않을경우\n네이버에서 가져오도록 하였습니다.", inline=False)
        embed.add_field(name="마지막으로..", value="시국이 시국인지라.. 다들 몸건강히 챙기시길바랍니다!\n긴글 읽어주셔서감사합니다!", inline=False)
        embed.set_footer(text=f"UTC {str(now.year)}년 {str(now.month)}월 {str(now.day)}일 {str(now.hour)}시 {str(now.minute)}분 {str(now.second)}초 Verified {ctx.author}", icon_url=ctx.author.avatar_url)
        channel = self.bot.get_channel(setchannel)
        await channel.send(embed = embed)

def setup(bot):
    bot.add_cog(Notice(bot))