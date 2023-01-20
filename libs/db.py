#!/usr/local/bin/python3
import mysql.connector

class Database():
    __db : mysql.connector.MySQLConnection

    def __init__(self, user:str, password:str,dbName:str ,host:str="localhost", port:str="3306"):
        self.__db =  mysql.connector.connect(
            host = host,
            port = port,
            user = user,
            password = password,
            database=dbName
        )

    def select(self, query:str) -> dict:
        """This method is designed to execute a SQL SELECT query.

        Args:
            query (str): The SQL query

        Returns:
            dict: A dict with the informations who were fetch on the database.
        """

        cursor = self.__db.cursor()
        cursor.execute(query)

        result = cursor.fetchall()

        return result

    def modify(self, query:str) -> None:
        """This method is designed to execute a SQL query (Insert or Update).

        Args:
            query (str): The SQL query
        """

        cursor = self.__db.cursor()
        cursor.execute(query)

        self.__db.commit()
