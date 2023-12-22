import os
import psycopg2

# Access the environment variables
hostIp = os.getenv("HOST")
database = os.getenv("POSTGRES_DB")
username = os.getenv("POSTGRES_USER")
userPassword = os.getenv("POSTGRES_PASSWORD")

def connectDBAndGiveCursor():
    try:
        conn = psycopg2.connect(dbname=database, user=username, password=userPassword, host=hostIp)
        conn.autocommit = True
        return conn.cursor()
    except psycopg2.Error as e:
        print(f"Error: {e}")