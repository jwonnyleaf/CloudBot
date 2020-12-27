import discord
from discord.ext import commands

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('faded'):
        await message.channel.send('is cool')

client.run('NzA0ODU4Mjg3NDE3MzI3NzU4.XqjQbw.LC3yJMD1cz8iosQRhEt0iwtU60c')
