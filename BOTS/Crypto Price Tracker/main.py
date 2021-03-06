import asyncio
import discord 
import json
from discord        import activity
from discord.ext    import tasks, commands
import secrets      as scrt
import blockchain   as blq
from discord.utils  import get
from aiohttp.client import request
from discord.ext    import commands
from discord.ext.commands.core import check, command


# Bot
bot   = commands.Bot(command_prefix = "!")
login = 0



# Login
@bot.event
async def on_ready():
    global login
    print('We have logged in as {0.user}'.format(bot))
    login = 1
    my_background_task.start()
    


# Bot Activity with Crypto Prices
@tasks.loop(seconds=120.0)
async def my_background_task():
    await bot.change_presence(activity=discord.Game(name='WoW'))
    await bot.change_presence(activity=discord.Game(name='Lost Ark'))



# Import Tokens Dict from blockchain.py
blq.tokens_dict



# Coin Price Command
@bot.command()
async def coin(ctx, arg1):
    if blq.tokens_dict == blq.tokens_dict :
        await blq.blockchain_connection (ctx, arg1)
    else:
        await ctx.reply("The token " + str(arg1) +  " is not in the token list, if you want to add " + str(arg1) + " to the list please use the command : " + '\n' + "!addtoken and insert key and value with an space on each")
        


# Add the token that you want
@bot.command()
async def add_token(ctx, key, value):

    if(key in blq.tokens_dict.keys()):
        await ctx.reply('I already have this token on my list, please add another Contract or another Value')
    else:
        blq.tokens_dict[key] = value
        await ctx.reply('Token added succesfuly')
 



bot.run(scrt.bot_token)

