from databaseConnect import connectDBAndGiveCursor
import psycopg2
from psycopg2 import sql

cursor = connectDBAndGiveCursor()

def vindVerhaalLijnKarakter(karakter_naam):
    try:
        #do query on DB and use psycopg2.sql to mitigate the risk of sql injection
        cursor.execute(sql.SQL("SELECT * FROM karakter k WHERE k.naam = %s \
                               INNER JOIN stripboek_karakter SK ON K.naam = SK.naam \
                               INNER JOIN stripboek S ON SK.naam = S.naam AND SK.issueNummer = S.Issuenummer \
                               ORDER BY S.uitgavedatum ASC"), (karakter_naam))
        output = cursor.fetchall()
        return(output)
    except psycopg2.Error as e:
        print(f"Error handeling sql query: {e}")
        return False
    
