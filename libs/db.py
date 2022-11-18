#!/usr/local/bin/python3
import mysql.connector, csv

class DbConnector:
    def __init__(self, crendentialsFile='dbCredentials'):
        with open(crendentialsFile, 'r') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',')
            for row in spamreader:
                self.database = mysql.connector.connect(
                  host=row[0],
                  port=row[1],
                  user=row[2],
                  password=row[3],
                  database=row[4]
                )

    def Select(self,query:str):
        Cursor = self.database.cursor()

        Cursor.execute(query)

        return Cursor.fetchall()

    def Insert(self, query:str):
        Cursor = self.database.cursor()

        Cursor.execute(query)

        database.commit()
