import discord
import os

from lib.imageMaker import ProfilImage

class Profile(discord.Cog):
    def __init__(self, bot) -> None:
        self._bot = bot

    @discord.slash_command(name="profile", description="Return your profile on server")
    async def profile(self, ctx):
        await ctx.defer()

        if isinstance(ctx.channel, discord.channel.TextChannel):
            user_id = str(ctx.author.id)
            guild_id = str(ctx.guild.id)
            username = ctx.author.name + "#" + ctx.author.discriminator
            userdisplayname = ctx.author.display_name
            userprofile = ctx.author.avatar.url

            img_profile = "data/img/profile/"
            img_background = "data/img/background/"

            self.__make_dir(img_profile)
            self.__make_dir(img_background)

            pro = ProfilImage(
                img_profile + user_id + ".png",
                username,
                userprofile,
                5,
                420,
                userdisplayname,
                background=img_background + "default"
            )
            await ctx.respond(file=discord.File(pro.ProfilPath()))
        else:
            await ctx.respond("You can only use this command in a server!")

    def __make_dir(self, dir):
        if not os.path.exists(dir):
            os.mkdir(dir)


def setup(bot):
    bot.add_cog(Profile(bot))
