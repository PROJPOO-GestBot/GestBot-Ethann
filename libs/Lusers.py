import os
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
        
    # private methods

