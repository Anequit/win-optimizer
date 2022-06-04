import ctypes
import os
import sys
import utils.registry as registry
import utils.parser as parser
import utils.powershell as powershell
from commands import commands

menu_options = [["1:", "Optimize Windows", "General performance and gaming optimizations"],
                ["2:", "Optimize Network", "Wi-Fi and Ethernet optimizations"],
                ["3:", "Disable Telemetry", "Disables telemetry data collection"],
                ["4:", "Disable Auto Updates", "Makes all updates manual"],
                ["5:", "Activate Windows Pro", "Activates Windows Pro edition for free"],
                ["6:", "System Cleanup", "Removes junk files"],
                ["7:", "Repair Corrupt Files", "Checks and repairs corrupted system files"],
                ["8:", "All of the above", "Chooses all options"],
                ["9:", "System Restore", "Opens system restore menu"]]

def print_commands() -> None:
    print(" Options".ljust(33), "Descriptions")
    print('-' * 82)
    
    for option in menu_options:
        print(f"| {option[0]} {option[1].ljust(26)} | {option[2].ljust(46)} |")
        
    print('-' * 82)
    print("\n[INFO] An automatic system restore point is created everytime, but only options 1-4 are reversable.\n")

def main() -> None:
    while(True):
        os.system("cls")
        print_commands()
        
        user_input = parser.parse_user_input(input("What would you like to do? [1-9]: "))
        print()
        
        if user_input == -1:
            continue
        
        elif user_input == 9:
            commands.restore()
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
        
        elif user_input == 8:
            commands.optimize_windows() 
            commands.optimize_network()
            commands.disable_telemetry()
            commands.disable_autoupdates()
            commands.activate_win_pro()
            commands.clean_system_junk()
            commands.repair_corruption()
            
        else:
            continue
            
        if input("\nWould you like to restart to apply changes (yes/no)? ") == "yes":
            powershell.execute_command(r"shutdown.exe /r /t 0")
        
if __name__ == "__main__":
    if ctypes.windll.shell32.IsUserAnAdmin() == False:
        print("I must be ran as administrator or I can't apply changes.")
        
        if input("Restart as admin (yes/no)? ") == "yes":
            powershell.execute_command(rf"Start-Process '{sys.argv[0]}' -Verb runAs")
            
        sys.exit()
        
    main()