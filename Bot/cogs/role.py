import discord
from discord.ext import commands

class Role(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        message_id = payload.message_id
        if message_id == 688746995120209995:
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g: g.id == guild_id, self.bot.guilds)
        
            if payload.emoji.name == '🔞':
                role = discord.utils.get(guild.roles, name='NSFW')
            else:
                role = discord.utils.get(guild.roles, name=payload.emoji.name)
            if role is not None:
                member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.add_roles(role)
                    print('add')
                else:
                    print("cant find user")
            else:
                print("do not have role")

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        message_id = payload.message_id
        if message_id == 688746995120209995:
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g: g.id == guild_id, self.bot.guilds)
        
            if payload.emoji.name == '🔞':
                role = discord.utils.get(guild.roles, name='NSFW')
            else:
                role = discord.utils.get(guild.roles, name=payload.emoji.name)
            if role is not None:
                member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.remove_roles(role)
                    print('remove')
                else:
                    print("cant find user")
            else:
                print("do not have role")


def setup(bot):
    bot.add_cog(Role(bot))