import winreg
import os
import datetime
import uuid
import utils.parser as parser
import utils.powershell as powershell
import keys
        
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
    if os.path.exists(APPDATA_PATH) == False:
        os.mkdir(APPDATA_PATH)
    
    backup_time = datetime.datetime.now()
    backup_path = os.path.join(APPDATA_PATH, str(uuid.uuid4()))
    
    os.mkdir(backup_path)
    
    try:
        for key in keys.backup_keys:
            keyname = key.split('\\')[-1]
            
            powershell.execute(f"reg export '{key}' '{backup_path}\{keyname}.reg'")
            
        with open(os.path.join(backup_path, "metadata"), 'w') as metadata:
            metadata.write(backup_time.strftime(f"%d/%m/%Y %H:%M:%S"))
    except:
        return False
            
    return True

def get_backups() -> list[tuple[str, str]]:
    backups = []
    
    for backup in os.listdir(APPDATA_PATH):
        with open(os.path.join(APPDATA_PATH, backup, "metadata"), 'r') as metadata:
            backups += [(backup, metadata.readline())]
    
    backups.reverse()
    
    return backups
    
def restore(backup_path: str) -> None:
    backup_path = os.path.join(APPDATA_PATH, backup_path)
    
    for key in keys.backup_keys:
        keyname = key.split('\\')[-1]
        
        print(f"reg import '{key}' '{backup_path}\{keyname}.reg'")
        powershell.execute(f"reg import '{key}' '{backup_path}\{keyname}.reg'")