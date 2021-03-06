from re import M
import discord
from discord.ext.commands.core import check, command
import emoji
from discord.ext import commands
from discord.utils import get

bot   = commands.Bot(command_prefix = "!")
login = 0

# Login
@bot.event
async def on_ready():
    global login
    print('We have logged in as {0.user}'.format(bot))
    login = 1

# Adding roles when react.
@bot.event
async def on_raw_reaction_add(payload):
    ChID = 922532325642866739

    if ChID == payload.channel_id:
        member = payload.member
        guild = member.guild
        emoji = payload.emoji.name

        if emoji == 'π¦ΈββοΈ':
            role = discord.utils.get(guild.roles, name = 'Valorant')
        elif emoji == 'β':
            role = discord.utils.get(guild.roles, name = 'World of Warcraft')
        elif emoji == 'π§ββοΈ':
            role = discord.utils.get(guild.roles, name = 'League of Legends')
        elif emoji == 'π«':
            role = discord.utils.get(guild.roles, name = 'Cs:Go')
        await member.add_roles(role)


# Removing roles when unreact. 
@bot.event
async def on_raw_reaction_remove(payload):
    ChID = 922532325642866739
    print("Removed rol to member.")
    if ChID == payload.channel_id:
        guild  = await(bot.fetch_guild(payload.guild_id))
        member = await(guild.fetch_member(payload.user_id))
        emoji = payload.emoji.name

        if emoji == 'π¦ΈββοΈ':
            role = discord.utils.get(guild.roles, name = 'Valorant')
        elif emoji == 'β':
            role = discord.utils.get(guild.roles, name = 'World of Warcraft')
        elif emoji == 'π§ββοΈ':
            role = discord.utils.get(guild.roles, name = 'League of Legends')
        elif emoji == 'π«':
            role = discord.utils.get(guild.roles, name = 'Cs:Go')
        await member.remove_roles(role)
        
# Message
@bot.command(pass_context = True)
async def setupRoles(ctx):
    embed   = discord.Embed(
    title   =  "Select your Game",
    description   =  "- Valorant π¦ΈββοΈ" + '\n' + "- World of Warcraft β" + '\n' + "- League of Legends π§ββοΈ" + '\n' + "- Cs:Go π«"
    )
    msg = await ctx.send(embed=embed)
    await msg.add_reaction('π¦ΈββοΈ')
    await msg.add_reaction('β')
    await msg.add_reaction('π§ββοΈ')
    await msg.add_reaction('π«')


bot.run("OTIwMzIxNTUzMTQzNTcwNDUy.YbiqPQ.wnN4lfjlxA-wef4h-fgoGX4IzJc")


