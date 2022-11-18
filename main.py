#!/usr/local/bin/python3
import discord
from libs.db import DbConnector

bot = discord.Bot()

db = DbConnector()

TOKEN = None
with open("key.txt","r") as key:
    TOKEN = key.readline()

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user)
    print(bot.user.id)
    print('------')

@bot.slash_command(name="ping",description="Say pong")
async def Ping(ctx):
    await ctx.respond("pong")

bot.run(TOKEN)
