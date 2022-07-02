from json import dumps
from fastapi import FastAPI
from settings import Settings
from version import Version

app = FastAPI()

@app.get("/settings")
def settings():
    return dumps(Settings().__dict__())

@app.get("/version")
def version():
    return Version.get_latest_version()