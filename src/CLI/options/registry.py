from utils.command import execute_command

def backup_registry() -> None:
    execute_command("powershell Enable-ComputerRestore -Drive 'C:\'")
    execute_command("powershell Checkpoint-Computer -Description win-optimizer -RestorePointType MODIFY_SETTINGS")

def restore_registry() -> None:
    execute_command("Rstrui.exe")
