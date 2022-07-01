from json import dumps
from fastapi import FastAPI
from settings import Settings


app = FastAPI()

@app.get("/")
def root():
    return dumps(Settings().__dict__())
