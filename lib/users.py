from lib.db import Database
import os

class Users():
    def __init__(self, user_id: str, guild_id: str):
        self.__db = Database(
            os.getenv("SQL_USERNAME"),
            os.getenv("SQL_USER_PASSWORD"),
            os.getenv("SQL_DB_NAME"),
            host=os.getenv("SQL_HOSTNAME"),
            port=os.getenv("SQL_PORT")
        )
        self.__user_id = user_id
        self.__guild_id = guild_id
        
    def get_user_id(self):
        return self.__user_id
    
    def get_guild_id(self):
        return self.__guild_id