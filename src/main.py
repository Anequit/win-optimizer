import ctypes
import os
import sys
import utils.registry as registry
import utils.parser as parser
import utils.powershell as powershell
from commands import commands

def print_commands() -> None:
    print("""
 Options\t\t\t  Descriptions
----------------------------------------------------------------------------------
| 1: Optimize Windows\t\t| General performance and gaming optimizations \t |
| 2: Optimize Network\t\t| Wi-Fi and Ethernet optimizations \t\t |
| 3: Disable Telemetry\t\t| Disables telemetry data collection \t\t |
| 4: Disable Auto Updates\t| Makes all updates manual \t\t\t |
| 5: Activate Windows 10/11 Pro\t| Activates Windows Pro edition for free \t |
| 6: System Cleanup\t\t| Removes junk files \t\t\t\t |
| 7: Repair Corrupt Files\t| Checks and repairs corrupted system files \t |
| 8: System Restore\t\t| Opens system restore menu \t\t\t |
----------------------------------------------------------------------------------

[WARNING] Only options 1-4 are reversable, but there is an automatic system restore point created.
""")

def print_backups(backups: list[tuple[str, str]]) -> None:
    print("-----------------------------------")
    
    for backup in range(len(backups)):
        if backup == 0:
            print(f"| {backup + 1}: {backups[backup][1]} [LATEST] |")
        
        else:
            print(f"| {backup + 1}: {backups[backup][1]} \t  |")
            
    print("-----------------------------------")
def main() -> None:
    while(True):
        os.system("cls")
        print_commands()
        
        user_input = parser.parse_user_input(input("What would you like to do? [1-8]: "))
        print()
        
        if user_input == -1:
            continue
        
        elif user_input == 8:
            backups = registry.get_backups()
            
            print_backups(backups)
            
            user_input = parser.parse_user_input(input(f"What would you like to do? [1-{len(backups)}]: "))
            
            if user_input > len(backups):
                continue
            
            registry.restore(backups[user_input - 1][0])
            continue
        
        print(" - Creating restore point.")

        backup_status = " - Successfully created restore point." if registry.backup() else " - Failed to create restore point."
        
        print(backup_status)
        
        if user_input == 1:
            commands.optimize_windows() 
            
        elif user_input == 2:
            commands.optimize_network()
            
        elif user_input == 3:
            commands.disable_telemetry()
            
        elif user_input == 4: 
            commands.disable_autoupdates()
            
        elif user_input == 5: 
            commands.activate_win_pro()
            
        elif user_input == 6: 
            commands.clean_system_junk()
            
        elif user_input == 7: 
            commands.repair_corruption()
            
        else:
            continue
            
        if input("\nWould you like to restart to apply changes (yes/no)? ") == "yes":
            powershell.execute(r"shutdown.exe /r /t 0")
        
if __name__ == "__main__":
    if ctypes.windll.shell32.IsUserAnAdmin() == False:
        print("I must be ran as administrator or I can't apply changes.")
        
        if input("Restart as admin (yes/no)? ") == "yes":
            powershell.execute(r"Start-Process '.\WinOptimizer.exe' -Verb runAs")
            
        sys.exit()
        
    main()