# Discord Tools
import discord
from discord.ext.commands.core import check, command
from discord.utils import get
from discord.ext import commands

# Requests
import requests

# Json
import json

# Time
import time

bot   = commands.Bot(command_prefix = "!")
login = 0

# Login
@bot.event
async def on_ready():
    global login
    print('We have logged in as {0.user}'.format(bot))
    login = 1


@bot.command()
async def coin(ctx, arg1):
    tokens_dict = {
            'Eternal' : '0xD44FD09d74cd13838F137B590497595d6b3FEeA4',
            'Slp'     : '0xcc8fa225d80b9c7d42f96e9570156c65d6caaa25',
            'Pvu'     : '0x31471e0791fcdbe82fbf4c44943255e923f1b794'
    }
    
    input_user = arg1.capitalize()
    
    if(input_user not in tokens_dict):
        token_query = await ctx.reply ("The token "+ str(input_user) + " is not in the list, if you want to add " + str(input_user) + " to the list please use the command : " + '\n' + 
        "!add_token")
    else: 
        url      =  "https://api.pancakeswap.info/api/v2/tokens/" + arg1.values()
        response =  requests.get(url)
        return json.loads(response.text)
        await ctx.reply ()
        
        
    

@bot.command()
async def add_token(ctx, arg1):   
    pass

        
    
    
    

bot.run("OTIyOTY2NTQ4Mzg4Mzg0ODE4.YcJJlQ.qDFXRfJW8Mby-aKuce6fOW-GoyM")