from utils.powershell import execute_commands, execute_command

def backup_registry() -> None:
    execute_command("Enable-ComputerRestore -Drive 'C:\'")
    execute_command("Checkpoint-Computer -Description win-optimizer -RestorePointType MODIFY_SETTINGS")

def restore_registry() -> None:
    execute_command("Rstrui.exe")
