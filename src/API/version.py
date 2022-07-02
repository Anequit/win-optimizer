from requests import get


class Version:
    @staticmethod
    def get_latest_version() -> str: 
        return get("https://api.github.com/repos/Anequit/win-optimizer/releases/latest").json()['tag_name']