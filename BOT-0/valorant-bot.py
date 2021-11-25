import discord
import webbrowser

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
    if(str(message.content) == "!Viper" or str(message.content) == "!viper"):
        await message.channel.send("Aquí tienes algunos lineups y trucos con Viper" + ("  https://blitz.gg/valorant/guides?agent=viper&difficulty=all&map=all&side=both&ability=all"))
    if(str(message.content) == "!Omen" or str(message.content) == "!omen"):
        await message.channel.send("Aquí tienes algunos lineups y trucos con Omen" + ("  https://blitz.gg/valorant/guides?agent=omen&difficulty=all&map=all&side=both&ability=all"))
    if(str(message.content) == "!Jett" or str(message.content) == "!jett"):
        await message.channel.send("Aquí tienes algunos lineups y trucos con Jett" + ("  https://blitz.gg/valorant/guides?agent=jett&difficulty=all&map=all&side=both&ability=all"))
    if(str(message.content) == "!Astra" or str(message.content) == "!astra"):
        await message.channel.send("Aquí tienes algunos lineups y trucos con Astra" + ("  https://blitz.gg/valorant/guides?agent=astra&difficulty=all&map=all&side=both&ability=all"))
    if(str(message.content) == "!Breach" or str(message.content) == "!breach"):
        await message.channel.send("Aquí tienes algunos lineups y trucos con Breach" + ("  https://blitz.gg/valorant/guides?agent=breach&difficulty=all&map=all&side=both&ability=all"))
    if(str(message.content) == "!Brimstone" or str(message.content) == "!brimstone"):
        await message.channel.send("Aquí tienes algunos lineups y trucos con Brimstone" + ("  https://blitz.gg/valorant/guides?agent=brimstone&difficulty=all&map=all&side=both&ability=all"))
    if(str(message.content) == "!Chamber" or str(message.content) == "!chamber"):
        await message.channel.send("Aquí tienes algunos lineups y trucos con Chamber" + ("  https://blitz.gg/valorant/guides?agent=chamber&difficulty=all&map=all&side=both&ability=all"))
    if(str(message.content) == "!Cypher" or str(message.content) == "!cypher"):
        await message.channel.send("Aquí tienes algunos lineups y trucos con Cypher" + ("  https://blitz.gg/valorant/guides?agent=cypher&difficulty=all&map=all&side=both&ability=all"))
    if(str(message.content) == "!Kayo" or str(message.content) == "!kayo"):
        await message.channel.send("Aquí tienes algunos lineups y trucos con KAY/O" + ("  https://blitz.gg/valorant/guides?agent=kayo&difficulty=all&map=all&side=both&ability=all"))
    if(str(message.content) == "!Killjoy" or str(message.content) == "!killjoy"):
        await message.channel.send("Aquí tienes algunos lineups y trucos con Killjoy" + ("  https://blitz.gg/valorant/guides?agent=killjoy&difficulty=all&map=all&side=both&ability=all"))
    if(str(message.content) == "!Phoenix" or str(message.content) == "!phoenix"):
        await message.channel.send("Aquí tienes algunos lineups y trucos con Phoenix" + ("  https://blitz.gg/valorant/guides?agent=phoenix&difficulty=all&map=all&side=both&ability=all"))
    if(str(message.content) == "!Raze" or str(message.content) == "!raze"):
        await message.channel.send("Aquí tienes algunos lineups y trucos con Raze" + ("  https://blitz.gg/valorant/guides?agent=raze&difficulty=all&map=all&side=both&ability=all"))
    if(str(message.content) == "!Reyna" or str(message.content) == "!reyna"):
        await message.channel.send("Aquí tienes algunos lineups y trucos con Reyna" + ("  https://blitz.gg/valorant/guides?agent=reyna&difficulty=all&map=all&side=both&ability=all"))
    if(str(message.content) == "!Sage" or str(message.content) == "!sage"):
        await message.channel.send("Aquí tienes algunos lineups y trucos con Sage" + ("  https://blitz.gg/valorant/guides?agent=sage&difficulty=all&map=all&side=both&ability=all"))
    if(str(message.content) == "!Sky" or str(message.content) == "!sky"):
        await message.channel.send("Aquí tienes algunos lineups y trucos con Sky" + ("  https://blitz.gg/valorant/guides?agent=skye&difficulty=all&map=all&side=both&ability=all"))
    if(str(message.content) == "!Sova" or str(message.content) == "!sova"):
        await message.channel.send("Aquí tienes algunos lineups y trucos con Sova" + ("  https://blitz.gg/valorant/guides?agent=sova&difficulty=all&map=all&side=both&ability=all"))
    if(str(message.content) == "!Yoru" or str(message.content) == "!yoru"):
        await message.channel.send("Aquí tienes algunos lineups y trucos con Yoru" + ("  https://blitz.gg/valorant/guides?agent=yoru&difficulty=all&map=all&side=both&ability=all"))


bot.run('Your Bot Code goes here')