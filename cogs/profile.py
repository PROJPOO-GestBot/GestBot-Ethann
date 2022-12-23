import discord
import os

from lib.imageMaker import ProfilImage


class Profile(discord.Cog):
    def __init__(self, bot) -> None:
        self._bot = bot

    @discord.slash_command(name="profile", description="Return your profile on server")
    async def profile(self, ctx):
        await ctx.defer()

        img_profile = "data/img/profile/"
        img_background = "data/img/background/"

        self.__make_dir(img_profile)
        self.__make_dir(img_background)

        pro = ProfilImage(
            img_profile + "386200134628671492.png",
            "Ethann8#7747",
            "https://cdn.discordapp.com/avatars/386200134628671492/a_de9e9a4c0e60276e7252e9b75c821b49.png",
            5,
            420,
            "Ethann",
            background=img_background + "default"
        )
        await ctx.respond(file=discord.File(pro.ProfilPath()))

    def __make_dir(self, dir):
        if not os.path.exists(dir):
            os.mkdir(dir)


def setup(bot):
    bot.add_cog(Profile(bot))
