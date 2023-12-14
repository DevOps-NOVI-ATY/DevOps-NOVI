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

# Create a delte old database
cursor.execute(f"DROP *;")

# Create a delte old database
cursor.execute(f"DROP USER {username};")

# Create a new database
cursor.execute(f"CREATE DATABASE {database};")

# Create a new user
cursor.execute(f"CREATE USER {username} WITH PASSWORD '{userPassword}';")
cursor.execute(f"SELECT * FROM pg_user;")
data = cursor.fetchall()
print(data)

cursor.execute(f"SELECT column_name, data_type, character_maximum_length FROM information_schema.columns WHERE table_name = 'pg_user';")
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
conn = psycopg2.connect(dbname=database, user=username, password=userPassword, host=hostIp)
conn.autocommit = True

cursor = conn.cursor()