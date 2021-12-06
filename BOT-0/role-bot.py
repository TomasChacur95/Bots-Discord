import discord
from discord.ext.commands.core import check, command
import emoji
from discord.ext import commands
from discord.utils import get


bot = commands.Bot(command_prefix = "!")
login = 0

@bot.event
async def on_ready():
    global login
    print('We have logged in as {0.user}'.format(bot))
    login = 1


@bot.command()
async def roles(ctx):
    reaction = await ctx.reply("Select your Game" + '\n' + '\n' + "- Valorant 🦸‍♀️" '\n' + "- World of Warcraft ⚔" + '\n' + "- League of Legends 🧙‍♀️" + '\n' + "- Cs:Go 🔫")
    valorant   = await reaction.add_reaction('🦸‍♀️')
    wow        = await reaction.add_reaction('⚔')
    league     = await reaction.add_reaction('🧙‍♀️')
    csgo       = await reaction.add_reaction('🔫')

    

    
    
    


bot.run("OTE1MzcwNjc4ODE4MDUwMTE5.YaanYA.Swt-8pvRnH9yxF9DYQ5MDGJ66Sg")
    
    

    



