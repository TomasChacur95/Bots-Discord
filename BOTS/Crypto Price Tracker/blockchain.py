import discord 
import json
import os
import aiohttp
from discord.utils  import get
from aiohttp.client import request



tokens_dict = {
    'morw'    :  '0x6b61b24504a6378e1a99d2aa2a5efcb1f5627a3a',
    'pvu'     :  '0x31471e0791fcdbe82fbf4c44943255e923f1b794',
    'eternal' :  '0xd44fd09d74cd13838f137b590497595d6b3feea4'
}

async def blockchain_connection(ctx, arg1):
    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://api.pancakeswap.info/api/v2/tokens/' + tokens_dict[arg1]) as r:
            res = await r.json()  # returns dict
            await ctx.reply(print(res['data']['price']))

            if r not in 'https://api.pancakeswap.info/api/v2/tokens/':
                ctx.reply("That token is not admited on this bot, please try with another one.")