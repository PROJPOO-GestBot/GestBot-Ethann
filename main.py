#!/usr/local/bin/python3
import discord
from libs.db import Database
import os,csv
from dotenv import load_dotenv

load_dotenv()


bot = discord.Bot()


"""
db = Database(
    os.getenv("SQL_USERNAME"),
    os.getenv("SQL_USER_PASSWORD"),
    os.getenv("SQL_DB_NAME"),
    host=os.getenv("SQL_HOSTNAME"),
    port=os.getenv("SQL_PORT")
)
"""


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user)
    print(bot.user.id)
    print('------')

bot.run(os.getenv("BOT_TOKEN"))
