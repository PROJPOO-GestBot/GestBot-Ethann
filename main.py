#!/usr/local/bin/python3
import discord
from libs.db import DbConnector
import os

bot = discord.Bot()

db = DbConnector()

TOKEN = None
with open("key.txt","r") as key:
    TOKEN = key.readline()

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user)
    print(bot.user.id)
    print('------')

bot.run(TOKEN)
