from fastapi import FastAPI
from src.API.settings import general_optimizations, network_optimizations, activation_commands
from requests import get


app = FastAPI()
optimizations = dict(general=general_optimizations(),
                     network=network_optimizations(),
                     activate=activation_commands())

@app.get("/optimizations")
def settings():
    return optimizations

@app.get("/version")
def version():
    return get("https://api.github.com/repos/Anequit/win-optimizer/releases/latest").json()['tag_name']