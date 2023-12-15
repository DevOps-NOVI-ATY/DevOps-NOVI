from fastapi import FastAPI
from config import conn

# Verbindingsgegevens voor de PostgreSQL-database

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "WelkomWelkomWelkom bij mijn eerste FastAPI API!"}

@app.get("/get_data_from_db")
async def get_data_from_db():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM jouw_tabel_naam")
    data = cursor.fetchall()
    cursor.close()
    return {"data": data}
    