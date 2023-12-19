from fastapi import FastAPI

app = FastAPI()

#GET request naar root endpoint.
@app.get("/")
async def root():
    return {"greeting":"Hello world"}



