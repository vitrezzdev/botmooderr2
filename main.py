import discord
from discord.ext import commands
import datetime

from urllib import parse, request
import re

bot = commands.Bot(command_prefix='-', description="O")


@bot.command()
async def sum(ctx, numOne: int, numTwo: int):
    await ctx.send(numOne + numTwo)


@bot.command()
async def info(ctx):
    embed = discord.Embed(title="𝐼𝑛𝑓𝑜 𝑀𝑜𝑜𝑑𝑒𝑟",
                          description="Tambien Poniendo Info 2!",
                          timestamp=datetime.datetime.utcnow(),
                          color=discord.Color.orange())
    embed.add_field(name="Twitch", value="https://www.twitch.tv/mooderfn")
    embed.add_field(name="Instagram Principal",
                    value="https://www.instagram.com/daviid_torresss/")
    embed.add_field(name="Instagram Secundario",
                    value="https://www.instagram.com/mooderfn/")
    embed.set_thumbnail(
        url=
        "https://cdn.discordapp.com/avatars/858375679182897213/a_1a65b9206920a5dc4bb01bf381b3043e.gif?size=128"
    )

    await ctx.send(embed=embed)


@bot.command()
async def info2(ctx):
    embed = discord.Embed(title="𝐼𝑛𝑓𝑜 𝑀𝑜𝑜𝑑𝑒𝑟",
                          description="Tambien Poniendo Info 2!",
                          timestamp=datetime.datetime.utcnow(),
                          color=discord.Color.orange())
    embed.add_field(name="Twitch", value="https://www.twitch.tv/mooderfn")
    embed.add_field(name="Instagram Principal",
                    value="https://www.instagram.com/daviid_torresss/")
    embed.add_field(name="Instagram Secundario",
                    value="https://www.instagram.com/mooderfn/")
    embed.set_thumbnail(
        url=
        "https://cdn.discordapp.com/avatars/858375679182897213/a_1a65b9206920a5dc4bb01bf381b3043e.gif?size=128"
    )

    await ctx.send(embed=embed)


@bot.event
async def on_ready():
  print('Started!')


@bot.listen()
async def on_message(message):
    if "-mooder" in message.content.lower():
        await message.channel.send('Que entrecejo tiene el cabron')
        await bot.process_commands(message)


@bot.listen()
async def on_message(message):
    if "-piriz" in message.content.lower():
        await message.channel.send('Que barriga mas gorda que tiene')
        await bot.process_commands(message)


@bot.listen()
async def on_message(message):
    if "-terne" in message.content.lower():
        await message.channel.send('Que nariz mas tuerta que tiene')
        await bot.process_commands(message)


@bot.listen()
async def on_message(message):
    if "-bernat" in message.content.lower():
        await message.channel.send('Sube el volumen a tu madre')
        await bot.process_commands(message)


@bot.listen()
async def on_message(message):
    if "-adri" in message.content.lower():
        await message.channel.send(
            'La cocaina es la aficion de algun familiar cercano')
        await bot.process_commands(message)


@bot.listen()
async def on_message(message):
    if "-pau" in message.content.lower():
        await message.channel.send('Le falta bastante pelo al calvo de mierda')
        await bot.process_commands(message)


@bot.listen()
async def on_message(message):
    if "-vitrezz" in message.content.lower():
        await message.channel.send('Que puto calvo de mierda')
        await bot.process_commands(message)


@bot.listen()
async def on_message(message):
    if "-biyaa" in message.content.lower():
        await message.channel.send(
            'Lo unico que ha hecho en la vida es decirle a MateoZ que tiene un tick en el ojo'
        )
        await bot.process_commands(message)


@bot.listen()
async def on_message(message):
    if "-richaa" in message.content.lower():
        await message.channel.send('Mongraal del mercadillo')
        await bot.process_commands(message)


@bot.listen()
async def on_message(message):
    if "-lynexx" in message.content.lower():
        await message.channel.send('Enfermo del Valorant y encima malo')
        await bot.process_commands(message)


@bot.listen()
async def on_message(message):
    if "-deca" in message.content.lower():
        await message.channel.send('La vascula es independentista, marca 155')
        await bot.process_commands(message)


@bot.listen()
async def on_message(message):
    if "-yepes" in message.content.lower():
        await message.channel.send('Mi hermano el Yepes es el mejor')
        await bot.process_commands(message)


@bot.listen()
async def on_message(message):
    if "-alco" in message.content.lower():
        await message.channel.send('Dice que ha follao y no ha hecho na')
        await bot.process_commands(message)


@bot.listen()
async def on_message(message):
    if "-maxond" in message.content.lower():
        await message.channel.send('No se pone la cam de lo feo que es')
        await bot.process_commands(message)


@bot.listen()
async def on_message(message):
    if "-marmol" in message.content.lower():
        await message.channel.send('Puto andaluz de mierda hijo de puta')
        await bot.process_commands(message)


@bot.listen()
async def on_message(message):
    if "-carles" in message.content.lower():
        await message.channel.send('Dice que se metera y nunca se mete')
        await bot.process_commands(message)


@bot.listen()
async def on_message(message):
    if "-kylian" in message.content.lower():
        await message.channel.send('Enano que le gusta repetir curso')
        await bot.process_commands(message)


@bot.listen()
async def on_message(message):
    if "-girozz" in message.content.lower():
        await message.channel.send('Le encantan las 07 al pedofilo')
        await bot.process_commands(message)


@bot.listen()
async def on_message(message):
    if "-pls pornhub" in message.content.lower():
        await message.channel.send(
            'https://es.pornhub.com/view_video.php?viewkey=ph5eb0a0e19dfb9')
        await message.channel.send(
            'https://es.pornhub.com/view_video.php?viewkey=ph60af8c5237304')
        await message.channel.send(
            'https://es.pornhub.com/view_video.php?viewkey=ph6058b5b603bd4')
        await message.channel.send(
            'https://es.pornhub.com/view_video.php?viewkey=ph5e907cc0ab793')
        await message.channel.send(
            'https://es.pornhub.com/view_video.php?viewkey=ph5a01d1e4d1d00')
        await message.channel.send(
            'https://es.pornhub.com/view_video.php?viewkey=ph5e4c260065cb6')
        await message.channel.send(
            'https://es.pornhub.com/view_video.php?viewkey=ph5c926e317c0d4')
        await message.channel.send(
            'https://es.pornhub.com/view_video.php?viewkey=ph5d11158690d58')
        await message.channel.send(
            'https://es.pornhub.com/view_video.php?viewkey=ph5ce55a0cdc738')
        await message.channel.send(
            'https://es.pornhub.com/view_video.php?viewkey=ph60295a113d070')
        await message.channel.send(
            'https://es.pornhub.com/view_video.php?viewkey=ph5ca4f79a6d5c9')
        await message.channel.send(
            'https://es.pornhub.com/view_video.php?viewkey=ph5d5a5defe18bd')
        await message.channel.send(
            'https://es.pornhub.com/view_video.php?viewkey=ph5ef5ef164dc09')
        await message.channel.send(
            'https://es.pornhub.com/view_video.php?viewkey=ph5faaabb0e2088')
        await message.channel.send(
            'https://es.pornhub.com/view_video.php?viewkey=ph60751013777bb')
        await message.channel.send(
            'https://es.pornhub.com/view_video.php?viewkey=ph5eff43d7a4b07')
        await message.channel.send(
            'https://es.pornhub.com/view_video.php?viewkey=ph5daf62d0cbf25')
        await message.channel.send(
            'https://es.pornhub.com/view_video.php?viewkey=ph5fa3ccb287f5e')
        await message.channel.send(
            'https://es.pornhub.com/view_video.php?viewkey=ph5e7c03edaf77f')
        await message.channel.send(
            'https://es.pornhub.com/view_video.php?viewkey=ph6021f5a439c94')
        await bot.process_commands(message)


bot.run('ODY0MjMyNTI0ODEyNTE3Mzg3.YOydQg.FN8tTcrO_exK9kTE8JkZTEzvXPg')
