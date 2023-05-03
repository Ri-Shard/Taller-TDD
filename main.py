from fastapi import FastAPI
from math import sqrt

app = FastAPI()

@app.get("/hello")
async def hello():
    return {"message": "Hello FastAPI"}