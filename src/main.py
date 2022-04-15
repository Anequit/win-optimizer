import ctypes
import os
import subprocess
import sys
import time
import winreg

software = []

registry_keys = [(r"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\AxInstSV\Start", 4, winreg.REG_DWORD),
                 (r"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\AppMgmt\Start", 4, winreg.REG_DWORD),
                 (r"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\CertPropSvc\Start", 4, winreg.REG_DWORD),
                 (r"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\PeerDistSvc\Start", 4, winreg.REG_DWORD),
                 (r"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\SCPolicySvc\Start", 4, winreg.REG_DWORD),
                 (r"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\SNMPTRAP\Start", 4, winreg.REG_DWORD),
                 (r"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\WebClient\Start", 4, winreg.REG_DWORD),
                 (r"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\WinRM\Start", 4, winreg.REG_DWORD),
                 (r"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\WerSvc\Start", 4, winreg.REG_DWORD),
                 (r"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\PNRPsvc\Start", 4, winreg.REG_DWORD),
                 (r"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\p2psvc\Start", 4, winreg.REG_DWORD),
                 (r"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\p2pimsvc\Start", 4, winreg.REG_DWORD),
                 (r"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\SysMain\DelayedAutoStart", 1, winreg.REG_DWORD),
                 (r"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\FileSystem\NtfsDisable8dot3NameCreation", 1, winreg.REG_DWORD),
                 (r"HKEY_CURRENT_USER\Control Panel\Desktop\HungAppTimeout", 4000, winreg.REG_DWORD),
                 (r"HKEY_CURRENT_USER\Control Panel\Desktop\WaitToKillAppTimeout", 5000, winreg.REG_DWORD),
                 (r"HKEY_CURRENT_USER\Control Panel\Desktop\MenuShowDelay", 400, winreg.REG_DWORD),
                 (r"HKEY_CURRENT_USER\Control Panel\Desktop\ForegroundLockTimeout", 200000, winreg.REG_DWORD),
                 (r"HKEY_CURRENT_USER\Control Panel\Desktop\AutoEndTasks", 1, winreg.REG_DWORD),
                 (r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Max Cached Icons", 2000, winreg.REG_DWORD),
                 (r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\NetworkThrottlingIndex", 4294967295, winreg.REG_DWORD),
                 (r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\SystemResponsiveness", 0, winreg.REG_DWORD),
                 (r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Games\Affinity", 0, winreg.REG_DWORD),
                 (r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Games\Background Only", "False", winreg.REG_SZ),
                 (r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Games\Clock Rate", 10000, winreg.REG_DWORD),
                 (r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Games\GPU Priority", 8, winreg.REG_DWORD),
                 (r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Games\Priority", 6, winreg.REG_DWORD),
                 (r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Games\Scheduling Category", "High", winreg.REG_SZ),
                 (r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Games\SFIO Priority", "High", winreg.REG_SZ),
                 (r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\MSMQ\Parameters\TCPNoDelay", 1, winreg.REG_DWORD),
                 (r"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management\LargeSystemCache", 0, winreg.REG_DWORD),
                 (r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Internet Explorer\MAIN\FeatureControl\FEATURE_MAXCONNECTIONSPER1_0SERVER\explorer.exe", 10, winreg.REG_DWORD),
                 (r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Internet Explorer\MAIN\FeatureControl\FEATURE_MAXCONNECTIONSPER1_0SERVER\iexplorer.exe", 10, winreg.REG_DWORD),
                 (r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Internet Explorer\MAIN\FeatureControl\FEATURE_MAXCONNECTIONSPERSERVER\explorer.exe", 10, winreg.REG_DWORD),
                 (r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Internet Explorer\MAIN\FeatureControl\FEATURE_MAXCONNECTIONSPERSERVER\iexplorer.exe", 10, winreg.REG_DWORD),
                 (r"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Tcpip\ServiceProvider\LocalPriority", 4, winreg.REG_DWORD),
                 (r"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Tcpip\ServiceProvider\HostsPriority", 5, winreg.REG_DWORD),
                 (r"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Tcpip\ServiceProvider\DnsPriority", 6, winreg.REG_DWORD),
                 (r"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Tcpip\ServiceProvider\NetbtPriority", 7, winreg.REG_DWORD),
                 (r"HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\Psched\NonBestEffortLimit", 0, winreg.REG_DWORD),
                 (r"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Tcpip\QoS\Do not use NLA", 1, winreg.REG_DWORD),
                 (r"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\LanmanServer\Parameters\Size", 3, winreg.REG_DWORD),
                 (r"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\MaxUserPort", 65534, winreg.REG_DWORD),
                 (r"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\TcpTimedWaitDelay", 30, winreg.REG_DWORD),
                 (r"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\DefaultTTL", 64, winreg.REG_DWORD),
                 (r"HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\Psched\TimerResolution", 0, winreg.REG_DWORD),
                 (r"HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\Psched\NonBestEffortLimit", 0, winreg.REG_DWORD),
                 (r"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Power\PowerThrottling\PowerThrottlingOff", 1, winreg.REG_DWORD)]


def parse_registry_path(fullpath: str) -> tuple[winreg.HKEYType, str, str]:
    root, split_path = fullpath.split('\\', 1)
    split_path, key = split_path.rsplit('\\', 1)

    if root.find("HKEY_CLASSES_ROOT") != -1:
        root = winreg.HKEY_CLASSES_ROOT

    elif root.find("HKEY_CURRENT_USER") != -1:
        root = winreg.HKEY_CURRENT_USER

    elif root.find("HKEY_LOCAL_MACHINE") != -1:
        root = winreg.HKEY_LOCAL_MACHINE

    elif root.find("HKEY_USERS") != -1:
        root = winreg.HKEY_USERS

    elif root.find("HKEY_CURRENT_CONFIG") != -1:
        root = winreg.HKEY_CURRENT_CONFIG

    return (root, split_path, key)

def write_value_to_registry_key(fullpath: str, value: str, value_type: int) -> None:
    root, path, key = parse_registry_path(fullpath)

    opened_key = winreg.CreateKeyEx(root, path, 0, winreg.KEY_ALL_ACCESS)
    winreg.SetValueEx(opened_key, key, 0, value_type, value)

def extract_network_interfaces() -> list[str]:
    items = []
    
    interfaces = winreg.OpenKeyEx(winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Interfaces", 0, winreg.KEY_READ)
    
    for x in range(100):
        try:
            items.append(winreg.EnumKey(interfaces, x))
            
        except:
            break
    
    return items

def optimize_network() -> None:
    os.system("PowerShell.exe Set-NetTCPSetting -SettingName internet -AutoTuningLevelLocal normal")
    os.system("PowerShell.exe Set-NetTCPSetting -SettingName internet -ScalingHeuristics disabled")
    os.system("netsh int tcp set supplemental internet congestionprovider=CUBIC")
    os.system("PowerShell.exe Set-NetOffloadGlobalSetting -ReceiveSegmentCoalescing disabled")
    os.system("PowerShell.exe Set-NetOffloadGlobalSetting -ReceiveSideScaling enabled")
    os.system("PowerShell.exe Disable-NetAdapterLso -Name *")
    os.system("PowerShell.exe Enable-NetAdapterChecksumOffload -Name *")
    os.system("PowerShell.exe Set-NetTCPSetting -SettingName internet -EcnCapability disabled")
    os.system("PowerShell.exe Set-NetOffloadGlobalSetting -Chimney disabled")
    os.system("PowerShell.exe Set-NetTCPSetting -SettingName internet -Timestamps disabled")
    os.system("PowerShell.exe Set-NetTCPSetting -SettingName internet -MaxSynRetransmissions 2")
    os.system("PowerShell.exe Set-NetTCPSetting -SettingName internet -NonSackRttResiliency disabled")
    os.system("PowerShell.exe Set-NetTCPSetting -SettingName internet -InitialRto 2000")
    os.system("PowerShell.exe Set-NetTCPSetting -SettingName internet -MinRto 300")
    os.system("netsh interface ipv4 set subinterface \"Ethernet\" mtu=1500 store=persistent")
    os.system("netsh interface ipv6 set subinterface \"Ethernet\" mtu=1500 store=persistent")
    os.system("netsh interface ipv4 set subinterface \"Wi-Fi\" mtu=1500 store=persistent")
    os.system("netsh interface ipv6 set subinterface \"Ethernet\" mtu=1500 store=persistent")
    
    for interface in extract_network_interfaces():
        write_value_to_registry_key(rf"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Interfaces\{interface}\TcpAckFrequency", 1, winreg.REG_DWORD)
        write_value_to_registry_key(rf"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Interfaces\{interface}\TcpDelAckTicks", 0, winreg.REG_DWORD)
        write_value_to_registry_key(rf"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Interfaces\{interface}\TCPNoDelay", 1, winreg.REG_DWORD)
    
    print(" - Network is now optimized.")

def optimize_windows() -> None:
    for item in registry_keys:
        write_value_to_registry_key(item[0], item[1], item[2])
        
    print(" - Windows is now optimized.")


def install_software() -> None:
    if len(software) == 0:
        print(" - No software listed in software.txt.")
        return

    for item in software:
        try:        
            subprocess.run(f"winget install -h \"{item}\"")
            
        except:
            print(f"{item} failed to install..")
            continue
        
    print(" - All software installed.")

def activate_win_pro() -> None:
    subprocess.run(r"powershell.exe slmgr.vbs /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX")
    subprocess.run(r"powershell.exe slmgr.vbs /skms kms8.msguides.com")
    subprocess.run(r"powershell.exe slmgr.vbs /ato")
    
    print(" - Windows is now activated.")

def disable_telemetry() -> None:
    write_value_to_registry_key(r"HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\DataCollection\AllowTelemetry", 0, winreg.REG_DWORD)
    write_value_to_registry_key(r"HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\TabletPC\PreventHandwritingDataSharing", 1, winreg.REG_DWORD)
    write_value_to_registry_key(r"HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\Psched\NonBestEffortLimit", 0, winreg.REG_DWORD)
    
    print(" - All telemetry disabled.")

def disable_autoupdates() -> None:
    write_value_to_registry_key(r"HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate\AU\AutoInstallMinorUpdates", 0, winreg.REG_DWORD)
    write_value_to_registry_key(r"HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate\AU\NoAutoUpdate", 1, winreg.REG_DWORD)
    write_value_to_registry_key(r"HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\WindowsStore\AutoDownload", 2, winreg.REG_DWORD)
    write_value_to_registry_key(r"HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate\SetAutoRestartNotificationDisable", 1, winreg.REG_DWORD)
    write_value_to_registry_key(r"HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\Maps\AutoDownloadAndUpdateMapData", 0, winreg.REG_DWORD)
    
    print(" - Auto updates disabled.")

def clean_system_junk() -> None:
    subprocess.run(r"cleanmgr.exe /verylowdisk /setup /autoclean")
    
    print(" - System junk has been removed.")

def main():
    menu = """
 Options\t\t\t  Descriptions
----------------------------------------------------------------------------------
| 1: Optimize Windows\t\t| General performance and gaming optimizations \t | 
| 2: Optimize Network\t\t| Wi-Fi and Ethernet optimizations \t\t |
| 3: Disable Telemetry\t\t| Disables telemetry data collection \t\t |
| 4: Disable Auto Updates\t| Makes all updates manual \t\t\t |
| 5: Install applications\t| Installs software located in software.txt \t |
| 6: Activate Windows 10/11 Pro\t| Activates Windows Pro edition for free \t |
| 7: System Cleanup\t\t| Removes junk files \t\t\t\t |
| 8: All of the above\t\t| Chooses all options \t\t\t\t |
----------------------------------------------------------------------------------
"""
    
    while(True):
        os.system("cls")
        print(menu)
        
        user_input = input("What would you like to do? [1-8]: ")
        print()
        
        if user_input.isdigit() == True:
            user_input = int(user_input)
            
            if user_input <= 0 or user_input >= 9:
                continue    
        
        else:
            continue
        
        if user_input == 1: optimize_windows()
        elif user_input == 2: optimize_network()
        elif user_input == 3: disable_telemetry()
        elif user_input == 4: disable_autoupdates()
        elif user_input == 5: install_software()
        elif user_input == 6: activate_win_pro()
        elif user_input == 7: clean_system_junk()
        elif user_input == 8:
            optimize_windows()
            optimize_network()
            disable_telemetry()
            disable_autoupdates()
            install_software()
            activate_win_pro()
            clean_system_junk()
            
        if input("\nWould you like to restart to apply changes (yes/no)? ") == "yes":
            subprocess.run(r"shutdown.exe /r /t 0")
        
        
if __name__ == "__main__":
    if ctypes.windll.shell32.IsUserAnAdmin() == False:
        print("I must be ran as administrator or I can't apply changes.")
        
        if input("Restart as admin (yes/no)? ") == "yes":
            subprocess.run(r"powershell.exe Start-Process '.\WinOptimizer.exe' -Verb runAs")
            
        sys.exit()
        
    if os.path.exists("software.txt") == True:
        with open("software.txt", 'r+') as f:
            software = f.readlines()
            f.close()
    
    main()