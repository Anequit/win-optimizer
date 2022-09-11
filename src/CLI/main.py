from sys import exit
from menu import *
from ctypes import windll
from os import name
from sys import executable, argv, exit
from options.registry import backup_registry


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

def main() -> None:
    if(is_windows() == False):
        print("This script is only designed to run on Windows operating systems.")
        input("Press any key to close..")
        exit(0)
        
    if(is_admin() == False):
        elevate_privileges()
        
    backup_registry()
    
    while(True):
        clear_screen()
        
        display_sections()
        section = get_section_input() - 1

        if section + 1 > len(menu_options):
            break
        
        clear_screen()
        
        display_options(menu_options[section])
        option = get_option_input(section) - 1

        if option + 1 > len(menu_options[section][2]):
            continue
        
        resolve_option(section, option)
        
if __name__ == "__main__":
    main()