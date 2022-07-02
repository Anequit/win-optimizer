from fastapi import FastAPI
from src.API.settings import Settings
from requests import get


app = FastAPI()

@app.get("/settings")
def settings():
    return Settings().__dict__()

@app.get("/version")
def version():
    return get("https://api.github.com/repos/Anequit/win-optimizer/releases/latest").json()['tag_name']