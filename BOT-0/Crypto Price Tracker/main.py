import discord 
import json
import aiohttp
import random
from discord        import activity
from discord.ext    import tasks, commands
import secrets      as scrt
from discord.utils  import get
from aiohttp.client import request
from discord.ext    import commands
from discord.ext.commands.core import check, command



# bot = scrt.bot
bot   = commands.Bot(command_prefix = "!")
login = 0



tokens_dict = {
    'morw' :     '0x6b61b24504a6378e1a99d2aa2a5efcb1f5627a3a',
    'slp'  :     '0xcc8fa225d80b9c7d42f96e9570156c65d6caaa25',
    'pvu'  :     '0x31471e0791fcdbe82fbf4c44943255e923f1b794',
    'eternal' :  '0xd44fd09d74cd13838f137b590497595d6b3feea4'
}

# Login
@bot.event
async def on_ready():
    global login
    print('We have logged in as {0.user}'.format(bot))
    login = 1
    my_background_task.start()

# Coin Price Command
@bot.command()
async def coin(ctx, arg1):
    global tokens_dict
    if tokens_dict == tokens_dict:
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://api.pancakeswap.info/api/v2/tokens/' + tokens_dict[arg1]) as r:
                res = await r.json()  # returns dict
                await ctx.reply(res['data']['price'])
    else:
        await ctx.reply("The token " + str(arg1) +  " is not in the token list, if you want to add " + str(arg1) + " to the list please use the command : " + '\n' + "!add_token and insert key and value with an space on each")
        


@bot.command()
async def add_token(ctx, key, value):
    global tokens_dict

    if(key in tokens_dict.keys()):
        await ctx.reply('I already have this token on my list, please add another Contract or another Value')
    else:
        tokens_dict[key] = value



@tasks.loop(seconds=120.0)
async def my_background_task():
    """Will loop every 60 seconds and change the bots presence"""
    await bot.change_presence(activity=discord.Game(name='XLS : '))
    await bot.change_presence(activity=discord.Game(name='BNB : '))



    

bot.run(scrt.bot_token)

