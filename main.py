from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "WelkomWelkomWelkom bij mijn eerste FastAPI API!"}