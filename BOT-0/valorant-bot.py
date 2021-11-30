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
async def agente (ctx, arg1):         
    if(arg1 != "viper" and arg1 != "omen" and arg1 != "jett" and arg1 != "astra" and arg1 != "breach" and arg1 != "brimstone" and arg1 != "chamber" 
    and arg1 != "cypher" and arg1 != "kayo" and arg1 != "killjoy" and arg1 != "phoenix" and arg1 != "raze" and arg1 != "reyna" and arg1 != "sage" and arg1 != "sky" 
    and arg1 != "sova" and arg1 != "yoru"):
        pido_agente = await ctx.reply("El Agente solicitado no existe, por favor ingresa un Agente valido.")
    else:
        pido_agente = await ctx.reply("Aquí tienes algunos lineups y trucos con "+ arg1.capitalize() + ("  https://blitz.gg/valorant/guides?agent=" + arg1.lower() + "&difficulty=all&map=all&side=both&ability=all"))
        
   
bot.run('Token')