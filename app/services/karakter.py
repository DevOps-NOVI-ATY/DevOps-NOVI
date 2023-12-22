from databaseConnect import connectDBAndGiveCursor
import psycopg2
from psycopg2 import sql

cursor = connectDBAndGiveCursor()

def vindVerhaalLijnKarakter(karakter_naam):
    try:
        #do query on DB and use psycopg2.sql to mitigate the risk of sql injection
        cursor.execute(sql.SQL(""))
    except psycopg2.Error as e:
        print(f"Error handeling sql query: {e}")
        return False