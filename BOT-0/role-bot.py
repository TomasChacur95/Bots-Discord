import discord
from discord.ext.commands.core import check, command
import emoji
from discord.ext import commands
from discord.utils import get


bot   = commands.Bot(command_prefix = "!")
login = 0

IDMensaje = 0

@bot.event
async def on_ready():
    global login
    print('We have logged in as {0.user}'.format(bot))
    login = 1



@bot.event
async def on_raw_reaction_add(ctx): 
    global IDMensaje
    if(IDMensaje == 0):
        print("No configuraste el BOT todavia...")
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


@bot.command()
async def setupRoles(ctx):
    global IDMensaje
    reaction   = await ctx.reply("Select your Game" + '\n' + '\n' + "- Valorant 🦸‍♀️" '\n' + "- World of Warcraft ⚔" + '\n' + "- League of Legends 🧙‍♀️" + '\n' + "- Cs:Go 🔫")
    IDMensaje  = reaction.message_id

    await reaction.add_reaction('🦸‍♀️')
    await reaction.add_reaction('⚔')
    await reaction.add_reaction('🧙‍♀️')
    await reaction.add_reaction('🔫')

    
bot.run("Your Code")
    
    

    



