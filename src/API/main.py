from fastapi import FastAPI
import src.API.settings as settings

app = FastAPI()

@app.get("/optimization")
def optimization():
    return settings.optimization

@app.get("/cleanup")
def cleanup():
    return settings.cleanup

@app.get("/telemetry")
def telemetry():
    return settings.telemetry

@app.get("/autoupdate")
def autoupdate():
    return settings.autoupdate

@app.get("/powerplan")
def powerplan():
    return settings.powerplan

@app.get("/activation")
def activation():
    return settings.activation

@app.get("/network")
def network():
    return settings.network