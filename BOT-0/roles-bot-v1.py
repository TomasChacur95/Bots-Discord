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

# Payload is a dictionary
@bot.event
async def on_raw_reaction_add(payload):
    ChID = 922532325642866739

    if ChID == payload.channel_id:
        member = payload.member
        guild = member.guild
        emoji = payload.emoji.name

        if emoji == '🦸‍♀️':
            role = discord.utils.get(guild.roles, name = 'Valorant')
        elif emoji == '⚔':
            role = discord.utils.get(guild.roles, name = 'World of Warcraft')
        elif emoji == '🧙‍♀️':
            role = discord.utils.get(guild.roles, name = 'League of Legends')
        elif emoji == '🔫':
            role = discord.utils.get(guild.roles, name = 'Cs:Go')
        await member.add_roles(role)
        

async def on_raw_reaction_remove(payload):
    ChID = 922532325642866739

    if ChID == payload.channel_id:
        guild = await(bot.fetch_guild(payload.guild_id))
        emoji = payload.emoji.name

        if emoji == '🦸‍♀️':
            role = discord.utils.get(guild.roles, name = 'Valorant')
        elif emoji == '⚔':
            role = discord.utils.get(guild.roles, name = 'World of Warcraft')
        elif emoji == '🧙‍♀️':
            role = discord.utils.get(guild.roles, name = 'League of Legends')
        elif emoji == '🔫':
            role = discord.utils.get(guild.roles, name = 'Cs:Go')
       
        member = await(guild.fetch_member(payload.user_id))
        
        if member is not None:
            await member.remove_roles(role)
        

@bot.command(pass_context = True)
async def setupRoles(ctx):
    embed   = discord.Embed(
    title   =  "Select your Game",
    description   =  "- Valorant 🦸‍♀️" + '\n' + "- World of Warcraft ⚔" + '\n' + "- League of Legends 🧙‍♀️" + '\n' + "- Cs:Go 🔫"
    )
    msg = await ctx.send(embed=embed)
    await msg.add_reaction('🦸‍♀️')
    await msg.add_reaction('⚔')
    await msg.add_reaction('🧙‍♀️')
    await msg.add_reaction('🔫')


bot.run("")


