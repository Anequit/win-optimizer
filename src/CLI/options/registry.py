from utils.command import execute_command
from rich.prompt import Confirm


def backup_registry() -> None:
    result = Confirm.ask("Would you like to backup the registry?", default=True, show_default=True)
    
    if(result == True):
        execute_command("powershell Enable-ComputerRestore -Drive 'C:\'")
        execute_command("powershell Checkpoint-Computer -Description win-optimizer -RestorePointType MODIFY_SETTINGS")

def restore_registry() -> None:
    execute_command("Rstrui.exe")
