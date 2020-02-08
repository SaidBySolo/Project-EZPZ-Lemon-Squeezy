import asyncio
import discord
from discord.ext import commands

class Vote(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def 투표(self, ctx, *args):
        args = [arg for arg in args]
        if not len(args):
            await ctx.send("`투표` `질문` `(옵션1)` `(옵션2)` `...`순으로 입력해주세요")
            return
        question = args[0]
        options = args[1:]
        if not options:
            options = ["네", "아니오"]
        optionEmojis = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣", "🔟"]

        desc = []
        desc.append("제목: {}".format(question))
        optionCnt = 0
        for option in options:
            desc.append("{}: {}".format(optionEmojis[optionCnt], options[optionCnt]))
            optionCnt += 1
        desc = "\n".join(desc)
        em = discord.Embed(colour=0xDEADBF, description=desc)
        name = ctx.author.nick
        if not name:
            name = ctx.author.name
        em.set_footer(text="생성자:{}".format(name), icon_url=ctx.author.avatar_url)
        msg = await ctx.send(embed=em)

        optionEmojis = optionEmojis[:len(options)]
        for emoji in optionEmojis:
            await msg.add_reaction(emoji)

        await asyncio.sleep(15)

        msg = await ctx.fetch_message(msg.id)

        reactions = {}
        for reaction in msg.reactions:
            reactions[reaction.emoji] = reaction.count

        result = discord.Embed(colour=0xDEADBF, title="결과:{}".format(question))
        optionCnt = 0
        for option in options:
            result.add_field(
                name="{}: {}".format(optionEmojis[optionCnt], options[optionCnt]),
                value="{}표".format(reactions.get(optionEmojis[optionCnt]) - 1)
            )
            optionCnt += 1

        await ctx.send(embed=result)

def setup(bot):
    bot.add_cog(Vote(bot))