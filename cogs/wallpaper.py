import discord

class Wallpaper(discord.Cog):
    def __init__(self, bot) -> None:
        self._bot = bot

    @discord.slash_command(name="wallpaper", description="To change/buy wallpaper")
    @discord.option("option", description="buy/change", choices=["change", "list"])
    @discord.option("wallpaper", description="Wallpaper specified")
    async def wallpaper(self, ctx, *, option:str, wallpaper:str):
        await ctx.defer()
        
        match option:
            case "change":
                pass
            case "list":
                pass
            
        
def setup(bot):
    bot.add_cog(Wallpaper(bot))
