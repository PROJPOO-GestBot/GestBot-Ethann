import unittest, os, sys
sys.path.insert(0,'..')
import GestBot.lib.imageMaker as ImageMaker

class Test_Image_Maker(unittest.TestCase):
    def Test_File_here(self):
        imgBackground = "img/background/"

        self.assertFalse(os.path.isfile(profilImage.ProfilPath))

        profilImage = ImageMaker.ProfilImage(
            "img/profil/unitTest.png", 
            "Test", 
            "https://cdn.discordapp.com/avatars/386200134628671492/a_de9e9a4c0e60276e7252e9b75c821b49.png",
            5,
            420,
            "Ethann",
            background=imgBackground+"default"
        )

        self.assertTrue(os.path.isfile(profilImage.ProfilPath))

        os.remove(profilImage.ProfilPath)