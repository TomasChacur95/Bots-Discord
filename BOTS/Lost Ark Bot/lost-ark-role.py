import discord
from discord.ext.commands.core import check, command
import emoji
from discord.ext import commands
from discord.utils import get
import secrets as scrt

bot   = commands.Bot(command_prefix = "+")
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
    ChID = 952334705347407875

    if ChID == payload.channel_id:
        member  = payload.member
        guild   = member.guild
        emoji   = payload.emoji.name

        if emoji == '🦸‍♀️':
            role = discord.utils.get(guild.roles, name = 'Deathblade')
        elif emoji == '⚔':
            role = discord.utils.get(guild.roles, name = 'Shadowhunter')
        elif emoji == '🧙‍♀️':
            role = discord.utils.get(guild.roles, name = 'Sorceress')
        elif emoji == '🔫':
            role = discord.utils.get(guild.roles, name = 'Bard')
        elif emoji == ':Berserker:':
            role = discord.utils.get(guild.roles, name = 'Berserker')
        elif emoji == '🧙‍♀️':
            role = discord.utils.get(guild.roles, name = 'Paladin')
        elif emoji == '🔫':
            role = discord.utils.get(guild.roles, name = 'Gunlancer')
        elif emoji == '⚔':
            role = discord.utils.get(guild.roles, name = 'Striker')
        elif emoji == '🧙‍♀️':
            role = discord.utils.get(guild.roles, name = 'Wardancer')
        elif emoji == '🔫':
            role = discord.utils.get(guild.roles, name = 'Scrapper')
        elif emoji == '⚔':
            role = discord.utils.get(guild.roles, name = 'Soulfist')
        elif emoji == '🧙‍♀️':
            role = discord.utils.get(guild.roles, name = 'Gunslinger')
        elif emoji == '<:Artillerist:>':
            role = discord.utils.get(guild.roles, name = 'Artillerist')
        elif emoji == '⚔':
            role = discord.utils.get(guild.roles, name = 'Deadeye')
        elif emoji == '🧙‍♀️':
            role = discord.utils.get(guild.roles, name = 'Sharpshooter')
        elif emoji == '🔫':
            role = discord.utils.get(guild.roles, name = 'Guild Master')
        
        
        await member.add_roles(role)


# Removing roles when unreact. 
@bot.event
async def on_raw_reaction_remove(payload):
    ChID = 952334705347407875
    print("Removed rol to member.")
    if ChID == payload.channel_id:
        guild   = await(bot.fetch_guild(payload.guild_id))
        member  = await(guild.fetch_member(payload.user_id))
        emoji   = payload.emoji.name

        if emoji == '🦹🏼‍♀️':
            role = discord.utils.get(guild.roles, name = 'Deathblade')
        elif emoji == '🧛🏼‍♀️':
            role = discord.utils.get(guild.roles, name = 'Shadowhunter')
        elif emoji == '🧙🏼‍♀️':
            role = discord.utils.get(guild.roles, name = 'Sorceress')
        elif emoji == '🧚🏼‍♂️':
            role = discord.utils.get(guild.roles, name = 'Bard')
        elif emoji == '⚔':
            role = discord.utils.get(guild.roles, name = 'Berserker')
        elif emoji == '🧙‍♀️':
            role = discord.utils.get(guild.roles, name = 'Paladin')
        elif emoji == ':shield:':
            role = discord.utils.get(guild.roles, name = 'Gunlancer')
        elif emoji == '⚔':
            role = discord.utils.get(guild.roles, name = 'Striker')
        elif emoji == '🧙‍♀️':
            role = discord.utils.get(guild.roles, name = 'Wardancer')
        elif emoji == '🔫':
            role = discord.utils.get(guild.roles, name = 'Scrapper')
        elif emoji == '⚔':
            role = discord.utils.get(guild.roles, name = 'Soulfist')
        elif emoji == '🧙‍♀️':
            role = discord.utils.get(guild.roles, name = 'Gunslinger')
        elif emoji == '🔫':
            role = discord.utils.get(guild.roles, name = 'Artillerist')
        elif emoji == '⚔':
            role = discord.utils.get(guild.roles, name = 'Deadeye')
        elif emoji == '🧙‍♀️':
            role = discord.utils.get(guild.roles, name = 'Sharpshooter')
        elif emoji == '🔫':
            role = discord.utils.get(guild.roles, name = 'Guild Master')
        
        await member.remove_roles(role)
        
# Message
@bot.command(pass_context = True)
async def setupRoles(ctx):
    embed   = discord.Embed(
    title   =  "Select your Game",
    description   =  "- Valorant 🦸‍♀️" + '\n' + "- World of Warcraft ⚔" + '\n' + "- League of Legends 🧙‍♀️" + '\n' + "- Cs:Go 🔫"
    )
    msg = await ctx.send(embed=embed)
    await msg.add_reaction('\N{Gunlancer}')
    await msg.add_reaction('\N{Shadowhunter}')
    await msg.add_reaction('\N{Sorceress}')
    await msg.add_reaction('\N{Bard}')
    await msg.add_reaction('\N{Berserker}')
    await msg.add_reaction('\N{Paladin}')
    await msg.add_reaction('\N{Gunlancer}')
    await msg.add_reaction('\N{Striker}')
    await msg.add_reaction('\N{Wardancer}')
    await msg.add_reaction('\N{Scrapper}')
    await msg.add_reaction('\N{Soulfist}')
    await msg.add_reaction('\N{Gunslinger}')
    await msg.add_reaction('\N{Artillerist}')
    await msg.add_reaction('\N{Deadeye}')
    await msg.add_reaction('\N{Sharpshooter}')
    await msg.add_reaction('\N{Guild Master}')
    


bot.run(scrt.bot_key)