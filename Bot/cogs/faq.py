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
        qtm = discord.Embed(title="DID", description=f"{message.author.id}", color=0x572271)
        qtm.set_thumbnail(url=message.author.avatar_url)
        qtm.add_field(name="문의자", value=f"{message.author}", inline=False)
        qtm.add_field(name="문의내용", value=f"{message.content}", inline=False)
        qtm.set_footer(text=f"문의일:(미국시간기준) {str(now.year)}년 {str(now.month)}월 {str(now.day)}일 {str(now.hour)}시 {str(now.minute)}분 {str(now.second)}초")
            await message.channel.send(embed = qtm)
        
def setup(bot):
    bot.add_cog(FAQ(bot))
