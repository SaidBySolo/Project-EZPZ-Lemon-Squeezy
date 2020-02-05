import discord
import asyncio
import datetime
from of.botembed import BotEmbed
from of.userdict import UserDict
from discord.ext import commands


class General():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(hidden=True)
    async def 핑(self):
        await self.bot.say(":ping_pong:퐁!")

    #Information command
    @commands.command(pass_context=True)
    async def 내정보(self, ctx):
        react_embed = UserDict.user_embed.get(ctx.author.id)
        if react_embed is not None: 
            await self.bot.say(embed = react_embed)
        else:
            await self.bot.say("엠베드가 존재하지않슴니다. 관리자에게 문의해주세요")


    @commands.command(pass_context=True)
    async def 투표(self, ctx, *args):
        args = [arg for arg in args]
        if not len(args):
            self.bot.say("`투표` `질문` `(옵션1)` `(옵션2)` `...`순으로 입력해주세용")
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
        msg = await self.bot.send_message(ctx.message.channel, embed=em)

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

        await self.bot.send_message(ctx.message.channel, embed=result)



 


def setup(bot):
    general = General(bot)
    bot.add_cog(general)