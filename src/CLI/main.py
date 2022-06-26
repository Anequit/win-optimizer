import ctypes
import os
import sys
from options import Options
from utils.powershell import Powershell
from utils.parser import Parser
from settings import Settings


menu_options = [["Optimize Windows", "General performance and gaming optimizations"],
                ["Optimize Network", "Wi-Fi and Ethernet optimizations"],
                ["Disable Telemetry", "Disables telemetry data collection"],
                ["Disable Auto Updates", "Makes all updates manual"],
                ["Activate Windows Pro", "Activates Windows Pro edition for free"],
                ["System Cleanup", "Removes junk files"],
                ["Repair Corrupt Files", "Checks and repairs corrupted system files"],
                ["All of the above", "Chooses all options"],
                ["System Restore", "Opens system restore menu"]]

def print_options() -> None:
    print(" Options".ljust(33), "Descriptions")
    print('-' * 82)
    
    for option in range(len(menu_options)):
        print(f"| {option + 1}: {menu_options[option][0].ljust(26)} | {menu_options[option][1].ljust(46)} |")
        
    print('-' * 82)
    print("\n[INFO] An automatic system restore point is created everytime, but only options 1-4 are reversable.\n")

def main() -> None:
    print("Loading settings..")
    Settings.load()
    
    while(True):
        os.system("cls")
        print_options()
        
        user_input = Parser.parse_user_input(input("What would you like to do? [1-9]: "))
        print()
        
        if user_input == 9:
            Options.restore()
            continue
        
        Options.backup()
        
        if user_input == 1:
            Options.optimize_windows() 
            
        elif user_input == 2:
            Options.optimize_network()
            
        elif user_input == 3:
            Options.disable_telemetry()
            
        elif user_input == 4: 
            Options.disable_autoupdates()
            
        elif user_input == 5: 
            Options.activate_win_pro()
            
        elif user_input == 6: 
            Options.clean_system_junk()
            
        elif user_input == 7: 
            Options.repair_corruption()
        
        elif user_input == 8:
            Options.optimize_windows() 
            Options.optimize_network()
            Options.disable_telemetry()
            Options.disable_autoupdates()
            Options.activate_win_pro()
            Options.clean_system_junk()
            Options.repair_corruption()
            
        else:
            continue
        
        if input("\nWould you like to restart to apply changes (yes/no)? ") == "yes":
            Powershell.execute_command(r"shutdown.exe /r /t 0")
        
if __name__ == "__main__":
    if ctypes.windll.shell32.IsUserAnAdmin() == False:
        print("I must be ran as administrator or I can't apply changes.")
        
        if input("Restart as admin (yes/no)? ") == "yes":
            Powershell.execute_command(rf"Start-Process '{sys.argv[0]}' -Verb runAs")
            
        sys.exit()
        
    main()