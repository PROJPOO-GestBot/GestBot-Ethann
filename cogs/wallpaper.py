import discord
from libs.Lusers import Lusers

class Wallpaper(discord.Cog):
    def __init__(self, bot) -> None:
        self._bot = bot

    @discord.slash_command(name="wallpaper", description="To change/buy wallpaper")
    @discord.option("option", description="list/change", choices=["change", "list"])
    @discord.option("wallpaper", description="Wallpaper specified", required=False)
    async def wallpaper(self, ctx, *, option:str, wallpaper:str):
        await ctx.defer()
                
        if isinstance(ctx.channel, discord.channel.TextChannel):
            user = Lusers(ctx.author.id, ctx.guild.id)

            match option:
                case "change":
                    pass
                case "list":
                    await ctx.respond(embed=self.__generate_embeb(user.get_list_posseded_wallpapers()))
                    
        else:
            await ctx.respond("You can only use this command in a server!")

    def __generate_embeb(self, wallpaperList) -> discord.Embed:
        description = ""
        
        for i in wallpaperList:
            description += "**" + str(i[0]) + "**\n"
        
        return discord.Embed(title="Wallpaper", description=description, color=0x75E6DA)
        
        

def setup(bot):
    bot.add_cog(Wallpaper(bot))
