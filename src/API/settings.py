from options import Options
from requests import get


class Settings:
    def __init__(self) -> None:
        self.options = Options().__dict__()
        self.latest = Settings.get_latest_version()
        
    def __dict__(self) -> dict[str]:
        return dict(options=self.options, latestVersion=self.latest)
    
    @staticmethod
    def get_latest_version() -> str:
        return get("https://api.github.com/repos/Anequit/win-optimizer/releases/latest").json()['tag_name']