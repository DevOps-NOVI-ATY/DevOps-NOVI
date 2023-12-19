from main import app

@app.get("/karakter")
async def root():
    return {"karakter":"Spiderman"}
