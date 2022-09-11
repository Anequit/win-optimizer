from ctypes import windll
from os import name
from sys import executable, argv, exit

def is_admin() -> bool:
    "Check for administrator privileges"
    
    return windll.Shell32.IsUserAnAdmin()

def elevate_privileges() -> None:
    "Elevate script to administrator privileges"

    windll.shell32.ShellExecuteW(None, "runas", executable, " ".join(argv), None, 1)
    exit(0)

def is_windows() -> bool:
    "Check if OS is Windows"
    
    # Check for NT
    if(name != "nt"):
        return False
    
    return True