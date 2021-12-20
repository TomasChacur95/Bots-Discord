import discord
from discord.ext.commands.core import check, command
import emoji
from discord.ext import commands
from discord.utils import get


bot   = commands.Bot(command_prefix = "!")
login = 0

IDMensaje = 0

# Login
@bot.event
async def on_ready():
    global login
    print('We have logged in as {0.user}'.format(bot))
    login = 1



@bot.event
async def on_raw_reaction_add(ctx): 
    global IDMensaje
    if(IDMensaje == 0):
        print("Bot is not configured yet")
        return 0
    emoji                = ctx.emoji
    if(ctx.message_id == IDMensaje and emoji == ":eye:"):
        print("Reaccion")


@bot.event
async def on_raw_reaction_add(ctx):
    lista_emojis = ["🦸‍♀️","⚔","🧙‍♀️","🔫"]
    alias_emojis = ["Valorant","WOW","LOL","CS"]
    global IDMensaje

    if(IDMensaje == ctx.message_id):
        #print("Reaccionaron al msg...")
        member = ctx.member
        guild  = ctx.guild
        emoji  = ctx.emoji.name
        if(emoji in lista_emojis):
            #print("Asigno rol de Valorant a " + str(member))
            nombre_rol = alias_emojis[lista_emojis.find(emoji)]
            role = discord.utils.get(guild.roles, name = nombre_rol)
            await member.add_roles(role)
@bot.event
async def on_raw_reaction_add(payload: discord.RawReactionActionEvent):
    ChID = 921480476886204487
    if payload.channel_id != ChID:
        return
    if str(payload.emoji) == '🦸‍♀️':
        valorant = discord.utils.get(payload.member.guild.roles, name="Valorant")
        await payload.member.add_roles(valorant)
    if str(payload.emoji) == '⚔':
        wow = discord.utils.get(payload.member.guild.roles, name="World of Warcraft")
        await payload.member.add_roles(wow)
    if str(payload.emoji) == '🧙‍♀️':
        league = discord.utils.get(payload.member.guild.roles, name="League of Legends")
        await payload.member.add_roles(league)
    if str(payload.emoji) == '🔫':
        csgo = discord.utils.get(payload.member.guild.roles, name="Cs:Go")
        await payload.member.add_roles(csgo)




@bot.command()
async def setupRoles(ctx):
    global IDMensaje
    
    reaction   = await ctx.reply("Select your Game" + '\n' + '\n' + "- Valorant 🦸‍♀️" '\n' + "- World of Warcraft ⚔" + '\n' + "- League of Legends 🧙‍♀️" + '\n' + "- Cs:Go 🔫")
    await reaction.add_reaction('🦸‍♀️')
    await reaction.add_reaction('⚔')
    await reaction.add_reaction('🧙‍♀️')
    await reaction.add_reaction('🔫')
    IDMensaje  = reaction.message_id


bot.run("")
    
    

    



