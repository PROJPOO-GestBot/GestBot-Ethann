#!/usr/local/bin/python3
import mysql

class DbConnector:
    def __init__(self):
        with open('credentials', 'r') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',')
            for row in spamreader:
                self.database = mysql.connector.connect(
                  host=row[0],
                  port=row[1],
                  user=row[2],
                  password=row[3],
                  database=row[4]
                )
    @property
    def Select(self,query):
        Cursor = self.database.cursor()

        Cursor.execute(query)

        return Cursor.fetchall()

    @Insert.setter
    def Insert(self, v):
        Cursor = self.database.cursor()

        Cursor.execute(v)

        database.commit()
