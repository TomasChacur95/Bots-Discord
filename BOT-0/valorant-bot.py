import discord
import webbrowser
from discord.ext import commands

bot = commands.Bot(command_prefix = "!")
inicio_sesion = 0

@bot.event
async def on_ready():
    global inicio_sesion
    print('We have logged in as {0.user}'.format(bot))
    inicio_sesion = 1

@bot.command()
async def agente(ctx, arg1):
    personajes = ["Astra", "Breach", "Brimstone", "Chamber", "Cypher", "Jett", "Kayo", "Killjoy", "Omen", "Phoenix", "Raze", "Reyna", "Sage", "Skye", "Sova", "Viper", "Yoru"]
    input_user = arg1.capitalize()
    if(input_user not in personajes):
        pido_agente = await ctx.reply("El Agente "+ str(input_user) + " no existe, por favor ingresa un Agente valido. " + "Aquí tienes una lista de todos los Agentes de Valorant: \n" + '\n'.join(personajes))
        
    else:
        pido_agente = await ctx.reply("Aquí tienes algunos lineups y trucos con " + input_user + ("  https://blitz.gg/valorant/guides?agent=" + input_user.lower() + "&difficulty=all&map=all&side=both&ability=all"))
        

bot.run('Token')