import os
import re 
from libs.db import Database

from dotenv import load_dotenv
load_dotenv()


class Lusers():

    # public methods
    def __init__(self, user_id, server_id):        
        self.__db = Database(
            os.getenv("SQL_USERNAME"),
            os.getenv("SQL_USER_PASSWORD"),
            os.getenv("SQL_DB_NAME"),
            host=os.getenv("SQL_HOSTNAME"),
            port=os.getenv("SQL_PORT")
        )
        self.__user_id = user_id
        self.__server_id = server_id
                
    def get_user_id(self):
        return self.__user_id
    
    def get_server_id(self):
        return self.__server_id
    
    def calcul_lvl(self, lvl, xp):
        if xp >= lvl * 10:
            return True
        return False
    
    def level(self):
        query = self.__select_profiles("Profils.level")
        return self.__db.select(query=query)[0][0]
    
    def xp(self):
        query = self.__select_profiles("Profils.xp")
        return self.__db.select(query=query)[0][0]
    
    def name_color(self):
        query = self.__select_profiles("Profils.nameColor")
        return self.__db.select(query=query)[0][0]
    
    def bar_color(self):
        query = self.__select_profiles("Profils.barColor")
        return self.__db.select(query=query)[0][0]

    def add_xp(self, xp=1):
        query = self.__select_profiles("Profils.id")
        
        current_id = self.__db.select(query=query)[0][0]
                
        self.__db.modify(query="UPDATE Profils " +
                            "SET xp = xp + " + str(xp) + 
                            "WHERE id = "+ str(current_id)+";")

    def remove_xp(self, number_xp):
        return

    def add_users(self):
        query = ("SELECT * FROM gestbot.users " +
                 "WHERE userId="+ str(self.__user_id) +";")
        if self.__db.select(query=query) == None:
            NotADirectoryError
            #crée profil pour new user
            
    def get_list_posseded_wallpapers(self):
            query = ("SELECT Wallpapers.name, Wallpapers.level FROM Profils " +
                    "INNER JOIN Users_makes_Profils ON Profils.id=Users_makes_Profils.Profils_id " +
                    "INNER JOIN Server_has_Profils ON Profils.id=Server_has_Profils.Profils_id " +
                    "INNER JOIN Users ON Users_makes_Profils.Users_id=Users.id " +
                    "INNER JOIN Server ON Server_has_Profils.Server_id=Server.id " +
                    "INNER JOIN Profils_has_Wallpapers ON Profils_has_Wallpapers.Profils_id=Profils.id " +
                    "INNER JOIN Wallpapers ON Wallpapers.id=Profils_has_Wallpapers.Wallpapers_id " + 
                    "WHERE Server.serverId = " + str(self.__server_id) + " AND Users.userId= " + str(self.__user_id) + ";")
            return self.__db.select(query=query)
        
    def current_wallpaper(self):
        query = self.__select_profiles("Wallpapers.name")
        return self.__db.select(query=query)[0][0]
    
    def change_wallpaper(self, wallpaper_name):
        query = ("SELECT Wallpapers.id FROM Wallpapers " +
                "WHERE Wallpapers.name = '" + wallpaper_name + "';")
        
        query_result = self.__db.select(query=query)
        
        if len(query_result) < 1:
            raise Exception("Wallpaper not found")
        
        wallpaper_id = query_result[0][0]
        
        profils_id = self.__db.select(query=self.__select_profiles("Profils.id"))[0][0]
        
        print(wallpaper_id)
        print(profils_id)
        
        if self.__wallpaper_is_posseded(wallpaper_name):
            query = ("UPDATE Profils " +
                "SET Wallpapers_id = " + str(wallpaper_id) + " " +
                "WHERE id = "+ str(profils_id)+";")
            
            self.__db.modify(query=query)
        else:
            raise Exception("Wallpaper not posseded")
    
    def change_bar_color(self, color, bar_color_or_name_color: bool=True):
        profils_id = self.__db.select(query=self.__select_profiles("Profils.id"))[0][0]

        hex_regex_check=re.findall(r'^#(?:[0-9a-fA-F]{3}){1,2}$|^#(?:[0-9a-fA-F]{3,4}){1,2}$',color)

        final_color = ""
    
        color_list = {
            "blue":"0000FF",
            "white":"FFFFFF",
            "black":"000000",
            "green":"00FF00",
            "yellow":"E6E600",
            "pink":"FF00FF",
            "red":"FF0000",
            "orange":"FF9900",
            "purple":"990099",
            "brown":"D2691E",
            "grey":"808080"
        }
        
        if hex_regex_check:
            final_color = hex_regex_check[0].replace("#","")
        elif color in color_list:
            final_color = color_list[color]
        else:
            raise Exception("Color not found")
        
        bar_name_color = ""
        
        if bar_color_or_name_color:
            bar_name_color = "barColor"
        else:
            bar_name_color = "nameColor"
        
        query = ("UPDATE Profils " +
            "SET " + bar_name_color + " = '" + final_color + "' " +
            "WHERE id = "+ str(profils_id)+";")
        self.__db.modify(query=query)
            
        
        return
    
    # public methods
    
    # private methods
    
    def __select_profiles(self, element):
        return ("SELECT " + element + " FROM Profils " + 
                "INNER JOIN Users_makes_Profils ON Profils.id = Users_makes_Profils.Profils_id " + 
                "INNER JOIN Server_has_Profils ON Profils.id = Server_has_Profils.Profils_id " + 
                "INNER JOIN Users ON Users_makes_Profils.Users_id = Users.id " + 
                "INNER JOIN Server ON Server_has_Profils.Server_id = Server.id " + 
                "INNER JOIN Wallpapers ON Profils.Wallpapers_id = Wallpapers.id " +
                "WHERE Server.serverId = " + str(self.__server_id) + " AND Users.userId = "+ str(self.__user_id) +";")
        
    def __wallpaper_is_posseded(self, wallpaper_name):
        for wallpaper in self.get_list_posseded_wallpapers():
            if wallpaper_name == wallpaper[0]:
                return True
        return False

        
    # private methods

