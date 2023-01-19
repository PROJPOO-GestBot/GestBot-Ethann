import discord

class Wallpaper(discord.Cog):
    def __init__(self, bot) -> None:
        self._bot = bot

    @discord.slash_command(name="wallpaper", description="To change/buy wallpaper")
    @discord.option("option", description="list/change", choices=["change", "list"])
    @discord.option("wallpaper", description="Wallpaper specified", required=False)
    async def wallpaper(self, ctx, *, option:str, wallpaper:str):
        await ctx.defer()
        
        if isinstance(ctx.channel, discord.channel.TextChannel):
            match option:
                case "change":
                    pass
                case "list":
                    pass
        else:
            await ctx.respond("You can only use this command in a server!")

def setup(bot):
    bot.add_cog(Wallpaper(bot))
