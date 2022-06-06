import requests
import json


class Keys:
    optimization_keys = None
    cleanup_keys = None
    telemetry_keys = None
    autoupdate_keys = None
    
    def load_keys() -> None:
        Keys.optimization_keys = json.loads(requests.get("https://win-optimizer-api.herokuapp.com/optimization").text)
        Keys.cleanup_keys = json.loads(requests.get("https://win-optimizer-api.herokuapp.com/cleanup").text)
        Keys.telemetry_keys = json.loads(requests.get("https://win-optimizer-api.herokuapp.com/telemetry").text)
        Keys.autoupdate_keys = json.loads(requests.get("https://win-optimizer-api.herokuapp.com/autoupdate").text)