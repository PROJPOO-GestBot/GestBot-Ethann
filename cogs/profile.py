import discord
import os

from lib.imageMaker import ProfilImage


class Profile(discord.Cog):
    def __init__(self, bot) -> None:
        self._bot = bot

    @discord.slash_command(name="profile", description="Return your profile on server")
    async def profile(self, ctx):
        await ctx.defer()

        # TODO this folder doesn't exist
        img_profile = "data/img/profile/"
        img_background = "data/img/background/"

        self.__make_dirs(img_profile)
        self.__make_dirs(img_background)

        #TODO Review Remove data from you code. You must using parameters to pass this kind of information.
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

    def __make_dirs(self, dirs):
        if not os.path.exists(dirs):
            os.makedirs(dirs)


def setup(bot):
    bot.add_cog(Profile(bot))
