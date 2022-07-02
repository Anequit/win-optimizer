from src.API.options import Options

class Settings:
    def __init__(self) -> None:
        self.options = Options().__dict__()
        
    def __dict__(self) -> dict[str]:
        return dict(options=self.options)