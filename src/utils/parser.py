import winreg

def parse_registry_path(fullpath: str) -> tuple[winreg.HKEYType, str, str]:
    root, split_path = fullpath.split('\\', 1)
    split_path, key = split_path.rsplit('\\', 1)

    if root.find("HKEY_CURRENT_USER") != -1:
        root = winreg.HKEY_CURRENT_USER

    elif root.find("HKEY_LOCAL_MACHINE") != -1:
        root = winreg.HKEY_LOCAL_MACHINE

    return (root, split_path, key)

def parse_user_input(user_input: str) -> int:
    try:
        user_input = int(user_input)
        
        if user_input <= 0:
            raise ValueError(f"user_input out of range")
    except:
        return -1
    
    return user_input