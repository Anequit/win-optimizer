from src.utils.command import execute_command
from rich.prompt import Confirm


def backup_registry(skip_prompt: bool = True) -> None:
    if not skip_prompt:
        result = Confirm.ask("Would you like to backup the registry?", default=True, show_default=True)
        
        # If user doesn't want to back up
        if not result:
            return

    execute_command("powershell Enable-ComputerRestore -Drive 'C:\'")
    execute_command("powershell Checkpoint-Computer -Description win-optimizer -RestorePointType MODIFY_SETTINGS")


def restore_registry() -> None:
    execute_command("Rstrui.exe")
