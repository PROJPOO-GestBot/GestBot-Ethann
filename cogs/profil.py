import discord, os
from libs.imageMaker import ProfilImage

class profil(discord.Cog):
    def __init__(self, bot) -> None:
        self._bot = bot

    @discord.slash_command(name="profil", description="Return your profil on server")
    async def profil(self, ctx):
        await ctx.defer()

        imgProfil = "img/profil/"
        imgBackground = "img/background/"

        self.__makeDirs(imgProfil)
        self.__makeDirs(imgBackground)

        pro = ProfilImage(
            imgProfil+"386200134628671492.png",
            "Ethann8#7747",
            "https://cdn.discordapp.com/avatars/386200134628671492/a_de9e9a4c0e60276e7252e9b75c821b49.png",
            5,
            420,
            "Ethann",
            background=imgBackground+"default"
        )
        await ctx.respond(file=discord.File(pro.ProfilPath()))

    def __makeDirs(self,dirs):
        if not os.path.exists(dirs):
            os.makedirs(dirs)

def setup(bot):
    bot.add_cog(profil(bot))
