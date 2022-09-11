from utils.powershell import Powershell


def backup() -> None:
    Powershell.execute_command("Enable-ComputerRestore -Drive 'C:\'")
    Powershell.execute_command("Checkpoint-Computer -Description win-optimizer -RestorePointType MODIFY_SETTINGS")

def restore() -> None:
    Powershell.execute_command("Rstrui.exe")
