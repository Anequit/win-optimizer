import winreg
import os
import utils.parser as parser
import utils.powershell as powershell
        
APPDATA_PATH = os.path.join(os.getenv("APPDATA"), "win-optimizer")

def write_keys(keys: list[tuple[str, int, any]]):
    for key in keys:
        write_key(key[0], key[1], key[2])

def write_key(fullpath: str, value: str, value_type: int) -> None:
    root, path, key = parser.parse_registry_path(fullpath)

    try:
        opened_key = winreg.CreateKeyEx(root, path, 0, winreg.KEY_ALL_ACCESS)
        
        winreg.SetValueEx(opened_key, key, 0, value_type, value)
    except:
        return
    
def delete_keys(keys: list[tuple[str, int, any]]):
    for key in keys:
        delete_key(key[0])    

def delete_key(fullpath: str) -> None:
    root, path, key = parser.parse_registry_path(fullpath)

    try:    
        opened_key = winreg.CreateKeyEx(root, path, 0, winreg.KEY_ALL_ACCESS)

        winreg.DeleteValue(opened_key, key)
    except:
        return
        
def backup() -> bool:
    try:
        powershell.execute("Enable-ComputerRestore -Drive 'C:\'",
                           "Checkpoint-Computer -Description win-optimizer -RestorePointType MODIFY_SETTINGS")
        
    except:
        return False
            
    return True

def restore() -> None:
    powershell.execute("Rstrui.exe")