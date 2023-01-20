import discord
from libs.Lusers import Lusers

class Wallpaper(discord.Cog):
    def __init__(self, bot) -> None:
        self._bot = bot

    @discord.slash_command(name="wallpaper", description="To change/buy wallpaper")
    @discord.option("option", description="list/change", choices=["change", "list", "Name Color", "Bar Color"])
    @discord.option("text", description="Wallpaper specified or name and bar color", required=False)
    async def wallpaper(self, ctx, *, option:str, text:str):
        await ctx.defer()
                
        if isinstance(ctx.channel, discord.channel.TextChannel):
            user = Lusers(ctx.author.id, ctx.guild.id)

            match option:
                case "change":
                    try: 
                        user.change_wallpaper(text)
                        await ctx.respond("Wallpaper changed!")
                    except Exception as e:
                        await ctx.respond(str(e))
                case "list":
                    await ctx.respond(embed=self.__generate_embeb(user.get_list_posseded_wallpapers()))
                case "Name Color":
                    try: 
                        user.change_bar_color(text, bar_color_or_name_color=False)
                        await ctx.respond("Name color changed!")
                    except Exception as e:
                        await ctx.respond(str(e))
                case "Bar Color":
                    try: 
                        user.change_bar_color(text)
                        await ctx.respond("Bar color changed!")
                    except Exception as e:
                        await ctx.respond(str(e))
                case _:
                    await ctx.respond("Option not found!")
                    
        else:
            await ctx.respond("You can only use this command in a server!")

    def __generate_embeb(self, wallpaperList) -> discord.Embed:
        description = ""
        
        for i in wallpaperList:
            description += "**" + str(i[0]) + "** (niveau obtenu : " + str(i[1]) + ")\n\n"
        
        return discord.Embed(title="Wallpaper", description=description, color=0x75E6DA)
        
        

def setup(bot):
    bot.add_cog(Wallpaper(bot))
