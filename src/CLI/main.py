from utils import system
from sys import exit
from menu import *

def main() -> None:
    if(system.is_windows() == False):
        print("This script is only designed to run on Windows operating systems.")
        input("Press any key to close..")
        exit(0)
        
    # FIXME: Make != into ==
    if(system.is_admin() != False):
        system.elevate_privileges()
        
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
