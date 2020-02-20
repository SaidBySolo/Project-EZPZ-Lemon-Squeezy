import datetime
import discord
from discord.ext import commands


class FAQ(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if not message.guild and message.author.id != 657604407021666304:
            now = datetime.datetime.now()
            qtu = discord.Embed(title="DID", description=f"{message.author.id}", color=0x572271)
            qtu.set_thumbnail(url=message.author.avatar_url)
            qtu.add_field(name="문의자", value=f"{message.author}", inline=False)
            qtu.add_field(name="문의내용", value=f"{message.content}", inline=False)
            qtu.set_footer(text=f"문의일:(미국시간기준) {str(now.year)}년 {str(now.month)}월 {str(now.day)}일 {str(now.hour)}시 {str(now.minute)}분 {str(now.second)}초")
            await message.channel.send("문의가 정상적으로 처리되었습니다.")
            channel = self.bot.get_channel(680105593817661486)
            await channel.send(embed = qtu)

    @commands.command()
    @commands.is_owner()
    async def 답변(self, ctx, *args):
        args = [arg for arg in args]
        if not len(args):
            await ctx.send("`답변` `DID` `답변내용` 순으로 입력해주세요")
            return
        now = datetime.datetime.now()
        atu = discord.Embed(title="처리자", description=f"{ctx.author}", color=0x572271)
        atu.set_thumbnail(url=ctx.author.avatar_url)
        atu.add_field(name="답변내용", value=f"{args[1]}", inline=False)
        atu.set_footer(text=f"답변일:(미국시간기준) {str(now.year)}년 {str(now.month)}월 {str(now.day)}일 {str(now.hour)}시 {str(now.minute)}분 {str(now.second)}초")
        channel = self.bot.get_channel(args[0])
        await channel.send(embed = atu)
        
def setup(bot):
    bot.add_cog(FAQ(bot))