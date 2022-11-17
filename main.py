#!/usr/local/bin/python3
import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

TOKEN = None
with open("key.txt","r") as key:
    TOKEN = key.readline()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run(TOKEN)
