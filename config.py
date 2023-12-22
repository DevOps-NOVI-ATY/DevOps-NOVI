import os
import psycopg2
from psycopg2 import sql

# Define the path to your .env file
dotenv_path = ".env"

# Check if the .env file exists
if os.path.exists(dotenv_path):
    # Open and read the .env file
    with open(dotenv_path, "r") as file:
        # Read each line and set environment variables
        for line in file:
            key, value = line.strip().split("=")
            os.environ[key] = value
else:
    print(".env file not found. Please create one.")

# Access the environment variables
superUser = os.getenv("SUPERUSER")
superUserPW = os.getenv("SUPERUSERPW")
hostIp = os.getenv("HOST")
database = os.getenv("DATABASE")
username = os.getenv("USERNAME")
userPassword = os.getenv("PASSWORD")
port = os.getenv("PORT")

conn = psycopg2.connect(dbname='postgres', user=superUser, password=superUserPW, host=hostIp)
conn.autocommit = True

# Create a cursor object to interact with the database
cursor = conn.cursor()

#check if db exists
def database_not_exists(database_name):
    try:
        cursor.execute(sql.SQL("SELECT 1 FROM pg_database WHERE datname = %s;"), (database_name,))
        return cursor.fetchone() is None
    except psycopg2.Error as e:
        print(f"Error checking if database '{database_name}' exists: {e}")
        return False

#TEMP REMOVE FOR PROD
cursor.execute(f"DROP DATABASE IF EXISTS {database};")
cursor.execute(f"DROP USER IF EXISTS {username};")

# Create a database
if(database_not_exists(database)):
    cursor.execute(f"CREATE DATABASE {database};")

#check if db exists
def user_not_exists(username):
    try:
        cursor.execute(sql.SQL("SELECT 1 FROM pg_user WHERE usename = %s;"), (username,))
        return cursor.fetchone() is None
    except psycopg2.Error as e:
        print(f"Error checking if user '{username}' exists: {e}")
        return False
    
# Create a user
if(user_not_exists(username)):
    cursor.execute(f"CREATE USER {username};")
    cursor.execute(f"ALTER USER {username} WITH ENCRYPTED PASSWORD '{userPassword}';")

#check users and tables
cursor.execute("SELECT * FROM pg_user;")
data = cursor.fetchall()
print(data)

# Grant privileges to the user on the new database
cursor.execute(f"GRANT ALL PRIVILEGES ON DATABASE {database} TO {username};")

# Commit the changes
conn.commit()

# Close the cursor and connection to the 'postgres' database
cursor.close()
conn.close()

# Now, establish a connection to the newly created database

