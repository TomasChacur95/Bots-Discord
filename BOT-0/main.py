import discord
from datetime import datetime

bot = discord.Client()

inicio_sesion = 0

@bot.event
async def on_ready():
    global inicio_sesion
    print('We have logged in as {0.user}'.format(bot))
    inicio_sesion = 1


@bot.event
async def on_message(message):
    print("Recibi un mensaje de : " + str(message.author) + " --> " + str(message.content))
    if(str(message.content) == "Hora" or str(message.content) == "hora"):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("Me esta pidiendo la hora --> " + str(current_time))
        await message.channel.send(current_time)




    '''
    if message.author == bot.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    '''
print("Antes de iniciar")







bot.run('OTEyNDE5Mzg5NTgyNzcwMjE2.YZvqxg.yYHA4QnepGjtg95E9CbUO5_yMlE')
print("Despues")