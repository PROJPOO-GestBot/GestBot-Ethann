import os
import discord
from dotenv import load_dotenv
import datetime

load_dotenv()
bot = discord.Bot()

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user)
    print(bot.user.id)
    print('------')

@bot.event
async def on_message(message):
    print("(in "+str(message.channel)+" at "+str(datetime.datetime.now())+")"+str(message.author)+": "+message.content)

bot.run(os.getenv("BOT_TOKEN"))
