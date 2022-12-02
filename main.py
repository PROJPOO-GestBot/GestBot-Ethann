#!/usr/local/bin/python3
import discord
from libs.db import Database
import os,csv
from dotenv import load_dotenv

load_dotenv()

bot = discord.Bot()

db = Database(os.getenv("sqlUser"), os.getenv("sqlPassword"), os.getenv("sqlDBName"), host=os.getenv("sqlHost"), port=os.getenv("sqlPort"))

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user)
    print(bot.user.id)
    print('------')

bot.run(os.getenv("token"))
