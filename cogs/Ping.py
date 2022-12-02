import discord

class Ping(discord.Cog):
    def __init__(self, bot) -> None:
        self._bot = bot

    @discord.slash_command()
    async def ping(self, ctx):
        await ctx.respond("pong")

def setup(bot):
    bot.add_cog(Ping(bot))
