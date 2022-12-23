import unittest, os, sys, hashlib
sys.path.insert(0,'..')
import GestBot.lib.imageMaker as ImageMaker

class Test_ImageMaker(unittest.TestCase):
    __imgBackground = "data/img/background/default"

    def test_is_there_a_file(self):

        self.assertFalse(os.path.isfile("data/img/profile/unitTest.png"))

        profilImage = ImageMaker.ProfilImage(
            "data/img/profile/unitTest.png", 
            "Test", 
            "https://cdn.discordapp.com/avatars/386200134628671492/a_de9e9a4c0e60276e7252e9b75c821b49.png",
            5,
            420,
            "Ethann",
            background=self.__imgBackground
        )

        self.assertTrue(os.path.isfile(profilImage.ProfilPath()))

        os.remove(profilImage.ProfilPath())
        
    def test_file_are_not_the_same(self):
        self.assertFalse(os.path.isfile("data/img/profile/unitTest.png"))
        self.assertFalse(os.path.isfile("data/img/profile/unitTest1.png"))

        profilImage = ImageMaker.ProfilImage(
            "data/img/profile/unitTest.png", 
            "Test", 
            "https://cdn.discordapp.com/avatars/386200134628671492/a_de9e9a4c0e60276e7252e9b75c821b49.png",
            5,
            420,
            "Ethann",
            background=self.__imgBackground
        )

        secondProfilImage = ImageMaker.ProfilImage(
            "data/img/profile/unitTest1.png", 
            "Test", 
            "https://cdn.discordapp.com/avatars/386200134628671492/a_de9e9a4c0e60276e7252e9b75c821b49.png",
            5,
            420,
            "Ethannnn",
            background=self.__imgBackground
        )
        
        self.assertTrue(os.path.isfile(profilImage.ProfilPath()))
        self.assertTrue(os.path.isfile(secondProfilImage.ProfilPath()))
        
        self.assertFalse(hashlib.md5(open(profilImage.ProfilPath()).read()) == hashlib.md5(open(secondProfilImage.ProfilPath()).read()))
        
        os.remove(profilImage.ProfilPath())
        os.remove(secondProfilImage.ProfilPath())
        
if __name__ == '__main__':
    unittest.main()