from utils.command import execute_command
from rich.prompt import Confirm


def backup_registry(skip_prompt: bool = False) -> None:
    if(skip_prompt == False):
        result = Confirm.ask("Would you like to backup the registry?", default=True, show_default=True)
        
        # Doesn't want to backup registry
        if(result == False):
            return
    
    execute_command("powershell Enable-ComputerRestore -Drive 'C:\'")
    execute_command("powershell Checkpoint-Computer -Description win-optimizer -RestorePointType MODIFY_SETTINGS")

def restore_registry() -> None:
    execute_command("Rstrui.exe")
