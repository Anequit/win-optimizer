import requests
import json


class Settings:
    optimization = None
    cleanup = None
    telemetry = None
    autoupdate = None
    powerplan = None
    activation = None
    network = None
    
    def load() -> None:
        Settings.optimization = json.loads(requests.get("https://win-optimizer-api.herokuapp.com/optimization").text)
        Settings.cleanup = json.loads(requests.get("https://win-optimizer-api.herokuapp.com/cleanup").text)
        Settings.telemetry = json.loads(requests.get("https://win-optimizer-api.herokuapp.com/telemetry").text)
        Settings.autoupdate = json.loads(requests.get("https://win-optimizer-api.herokuapp.com/autoupdate").text)
        Settings.powerplan = json.loads(requests.get("https://win-optimizer-api.herokuapp.com/powerplan").text)
        Settings.activation = json.loads(requests.get("https://win-optimizer-api.herokuapp.com/activation").text)
        Settings.network = json.loads(requests.get("https://win-optimizer-api.herokuapp.com/network").text)