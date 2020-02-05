import discord
import asyncio
import datetime
from discord.ext import commands

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(hidden=True)
    async def 핑(self, ctx):
        await ctx.send(":ping_pong:퐁!")

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
        optionEmojis = ["1⃣", "2⃣", "3⃣", "4⃣", "5⃣", "6⃣", "7⃣", "8⃣", "9⃣", "🔟"]

        desc = []
        desc.append("🤔: {}?".format(question))
        optionCnt = 0
        for option in options:
            desc.append("{}: {}".format(optionEmojis[optionCnt], options[optionCnt]))
            optionCnt += 1
        desc = "\n".join(desc)
        em = discord.Embed(colour=0xDEADBF, description=desc)
        name = ctx.message.author.nick
        if not name:
            name = ctx.message.author.name
        em.set_footer(text="생성자{}".format(name), icon_url=ctx.message.author.avatar_url)
        msg = await ctx.send(ctx.message.channel, embed=em)

        optionEmojis = optionEmojis[:len(options)]
        for emoji in optionEmojis:
            await self.bot.add_reaction(msg, emoji)

        await asyncio.sleep(60)

        msg = await self.bot.get_message(ctx.message.channel, msg.id)

        reactions = {}
        for reaction in msg.reactions:
            reactions[reaction.emoji] = reaction.count

        result = discord.Embed(colour=0xDEADBF, title="🤔:에대한결과입니다{}".format(question))
        optionCnt = 0
        for option in options:
            result.add_field(
                name="{}: {}".format(optionEmojis[optionCnt], options[optionCnt]),
                value="{}표".format(reactions.get(optionEmojis[optionCnt]) - 1)
            )
            optionCnt += 1

        await ctx.send(ctx.message.channel, embed=result)

