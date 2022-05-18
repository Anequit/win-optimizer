import ctypes
import os
import subprocess
import sys
import winreg
import shutil

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
                 (r"HKEY_CURRENT_USER\Control Panel\Desktop\HungAppTimeout", "4000", winreg.REG_SZ),
                 (r"HKEY_CURRENT_USER\Control Panel\Desktop\WaitToKillAppTimeout", "5000", winreg.REG_SZ),
                 (r"HKEY_CURRENT_USER\Control Panel\Desktop\MenuShowDelay", "0", winreg.REG_SZ),
                 (r"HKEY_CURRENT_USER\Control Panel\Desktop\ForegroundLockTimeout", 200000, winreg.REG_DWORD),
                 (r"HKEY_CURRENT_USER\Control Panel\Desktop\AutoEndTasks", "1", winreg.REG_SZ),
                 (r"HKEY_CURRENT_USER\Control Panel\Mouse\MouseHoverTime", "100", winreg.REG_SZ),
                 (r"HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\DesktopProcess", 1, winreg.REG_DWORD),
                 (r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Dfrg\BootOptimizeFunction\Enable", "Y", winreg.REG_SZ),
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
                 (r"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management\LargeSystemCache", 1, winreg.REG_DWORD),
                 (r"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Tcpip\ServiceProvider\LocalPriority", 4, winreg.REG_DWORD),
                 (r"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Tcpip\ServiceProvider\HostsPriority", 5, winreg.REG_DWORD),
                 (r"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Tcpip\ServiceProvider\DnsPriority", 6, winreg.REG_DWORD),
                 (r"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Tcpip\ServiceProvider\NetbtPriority", 7, winreg.REG_DWORD),
                 (r"HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\Psched\NonBestEffortLimit", 0, winreg.REG_DWORD),
                 (r"HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\Psched\TimerResolution", 0, winreg.REG_DWORD),
                 (r"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Tcpip\QoS\Do not use NLA", "1", winreg.REG_SZ),
                 (r"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\LanmanServer\Parameters\Size", 3, winreg.REG_DWORD),
                 (r"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\MaxUserPort", 65534, winreg.REG_DWORD),
                 (r"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\TcpTimedWaitDelay", 30, winreg.REG_DWORD),
                 (r"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\DefaultTTL", 64, winreg.REG_DWORD),
                 (r"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Power\PowerThrottling\PowerThrottlingOff", 1, winreg.REG_DWORD),
                 (r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Internet Explorer\Main\FeatureControl\FEATURE_MAXCONNECTIONSPERSERVER\explorer.exe", 10, winreg.REG_DWORD),
                 (r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Internet Explorer\Main\FeatureControl\FEATURE_MAXCONNECTIONSPER1_0SERVER\explorer.exe", 10, winreg.REG_DWORD),
                 (r"HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\BackgroundAccessApplications\GlobalUserDisabled", 1, winreg.REG_DWORD),
                 (r"HKEY_CURRENT_USER\System\GameConfigStore\GameDVR_Enabled", 0, winreg.REG_DWORD),
                 (r"HKEY_CURRENT_USER\System\GameConfigStore\GameDVR_FSEBehaviorMode", 2, winreg.REG_DWORD),
                 (r"HKEY_CURRENT_USER\System\GameConfigStore\GameDVR_HonorUserFSEBehaviorMode", 0, winreg.REG_DWORD),
                 (r"HKEY_CURRENT_USER\System\GameConfigStore\GameDVR_DXGIHonorFSEWindowsCompatible", 1, winreg.REG_DWORD),
                 (r"HKEY_CURRENT_USER\System\GameConfigStore\GameDVR_EFSEFeatureFlags", 0, winreg.REG_DWORD)]

cleanup_keys = [(r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\VolumeCaches\Active Setup Temp Folders\StateFlags0000", 2, winreg.REG_DWORD),
                (r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\VolumeCaches\BranchCache\StateFlags0000", 2, winreg.REG_DWORD),
                (r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\VolumeCaches\D3D Shader Cache\StateFlags0000", 2, winreg.REG_DWORD),
                (r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\VolumeCaches\Delivery Optimization Files\StateFlags0000", 2, winreg.REG_DWORD),
                (r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\VolumeCaches\Diagnostic Data Viewer database files\StateFlags0000", 2, winreg.REG_DWORD),
                (r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\VolumeCaches\Downloaded Program Files\StateFlags0000", 2, winreg.REG_DWORD),
                (r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\VolumeCaches\Feedback Hub Archive log files\StateFlags0000", 2, winreg.REG_DWORD),
                (r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\VolumeCaches\Internet Cache Files\StateFlags0000", 2, winreg.REG_DWORD),
                (r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\VolumeCaches\Language Pack\StateFlags0000", 2, winreg.REG_DWORD),
                (r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\VolumeCaches\Old ChkDsk Files\StateFlags0000", 2, winreg.REG_DWORD),
                (r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\VolumeCaches\RetailDemo Offline Content\StateFlags0000", 2, winreg.REG_DWORD),
                (r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\VolumeCaches\Setup Log Files\StateFlags0000", 2, winreg.REG_DWORD),
                (r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\VolumeCaches\System error memory dump files\StateFlags0000", 2, winreg.REG_DWORD),
                (r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\VolumeCaches\System error minidump files\StateFlags0000", 2, winreg.REG_DWORD),
                (r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\VolumeCaches\Temporary Files\StateFlags0000", 2, winreg.REG_DWORD),
                (r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\VolumeCaches\Temporary Setup Files\StateFlags0000", 2, winreg.REG_DWORD),
                (r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\VolumeCaches\Thumbnail Cache\StateFlags0000", 2, winreg.REG_DWORD),
                (r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\VolumeCaches\Update Cleanup\StateFlags0000", 2, winreg.REG_DWORD),
                (r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\VolumeCaches\User file versions\StateFlags0000", 2, winreg.REG_DWORD),
                (r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\VolumeCaches\Windows Defender\StateFlags0000", 2, winreg.REG_DWORD),
                (r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\VolumeCaches\Windows Error Reporting Files\StateFlags0000", 2, winreg.REG_DWORD)]

telemetry_keys =[(r"HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\DataCollection\AllowTelemetry", 0, winreg.REG_DWORD),
                (r"HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\TabletPC\PreventHandwritingDataSharing", 1, winreg.REG_DWORD),
                (r"HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\Psched\NonBestEffortLimit", 0, winreg.REG_DWORD),
                (r"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\DiagTrack\Start", 4, winreg.REG_DWORD),
                (r"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\dmwappushservice\Start", 4, winreg.REG_DWORD),
                (r"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\diagsvc\Start", 4, winreg.REG_DWORD),
                (r"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\diagnosticshub.standardcollector.service\Start", 4, winreg.REG_DWORD)]

def run(commands: list):
    for command in commands:
        try:
            subprocess.check_output(["powershell.exe", command], stderr=None)
        except: 
            continue

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

def delete_registry_key(fullpath: str) -> None:
    root, path, key = parse_registry_path(fullpath)

    opened_key = winreg.CreateKeyEx(root, path, 0, winreg.KEY_ALL_ACCESS)
    try:
        winreg.DeleteValue(opened_key, key)
    except:
        return

def optimize_network() -> None:
    run(["Set-NetTCPSetting -SettingName internet -AutoTuningLevelLocal normal",
        "Set-NetTCPSetting -SettingName internet -ScalingHeuristics disabled",
        "netsh int tcp set supplemental internet congestionprovider=CUBIC",
        "Set-NetOffloadGlobalSetting -ReceiveSegmentCoalescing disabled",
        "Set-NetOffloadGlobalSetting -ReceiveSideScaling enabled",
        "Disable-NetAdapterLso -Name *",
        "Enable-NetAdapterChecksumOffload -Name *",
        "Set-NetTCPSetting -SettingName internet -EcnCapability disabled",
        "Set-NetOffloadGlobalSetting -Chimney disabled",
        "Set-NetTCPSetting -SettingName internet -Timestamps disabled",
        "Set-NetTCPSetting -SettingName internet -MaxSynRetransmissions 2",
        "Set-NetTCPSetting -SettingName internet -NonSackRttResiliency disabled",
        "Set-NetTCPSetting -SettingName internet -InitialRto 2000",
        "Set-NetTCPSetting -SettingName internet -MinRto 300",
        "netsh interface ipv4 set subinterface \"Ethernet\" mtu=1500 store=persistent",
        "netsh interface ipv6 set subinterface \"Ethernet\" mtu=1500 store=persistent",
        "netsh interface ipv4 set subinterface \"Wi-Fi\" mtu=1500 store=persistent",
        "netsh interface ipv6 set subinterface \"Wi-Fi\" mtu=1500 store=persistent"])
    
    print(" - Network is now optimized.")

def optimize_windows() -> None:
    for item in registry_keys:
        write_value_to_registry_key(item[0], item[1], item[2])
    
    run(["powercfg /s 381b4222-f694-41f0-9685-ff5bb260df2e",
        "powercfg /d 010fd358-aaf5-4687-a504-26218b58eab8",
        "powercfg /duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61 010fd358-aaf5-4687-a504-26218b58eab8",
        "powercfg /changename 010fd358-aaf5-4687-a504-26218b58eab8 \"Optimized Ultimate Performance\"",
        "powercfg /setacvalueindex 010fd358-aaf5-4687-a504-26218b58eab8 54533251-82be-4824-96c1-47b60b740d00 893dee8e-2bef-41e0-89c6-b55d0929964c 0",
        "powercfg /setdcvalueindex 010fd358-aaf5-4687-a504-26218b58eab8 54533251-82be-4824-96c1-47b60b740d00 893dee8e-2bef-41e0-89c6-b55d0929964c 0",
        "powercfg /setacvalueindex 010fd358-aaf5-4687-a504-26218b58eab8 7516b95f-f776-4464-8c53-06167f40cc99 3c0bc021-c8a8-4e07-a973-6b14cbcb2b7e 384",
        "powercfg /setdcvalueindex 010fd358-aaf5-4687-a504-26218b58eab8 7516b95f-f776-4464-8c53-06167f40cc99 3c0bc021-c8a8-4e07-a973-6b14cbcb2b7e 258",
        "powercfg /setacvalueindex 010fd358-aaf5-4687-a504-26218b58eab8 238c9fa8-0aad-41ed-83f4-97be242c8f20 29f6c1db-86da-48c5-9fdb-f2b67b1f44da 708",
        "powercfg /setdcvalueindex 010fd358-aaf5-4687-a504-26218b58eab8 238c9fa8-0aad-41ed-83f4-97be242c8f20 29f6c1db-86da-48c5-9fdb-f2b67b1f44da 384",
        "powercfg /s 010fd358-aaf5-4687-a504-26218b58eab8",
        "powercfg /hibernate off",
        "Disable-MMAgent -MemoryCompression"])
    
    print(" - Windows is now optimized.")

def activate_win_pro() -> None:
    run([r"slmgr.vbs /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX",
        r"slmgr.vbs /skms kms8.msguides.com",
        r"slmgr.vbs /ato"])
    
    print(" - Windows is now activated.")

def disable_telemetry() -> None:
    for item in telemetry_keys:
        write_value_to_registry_key(item[0], item[1], item[2])
    
    print(" - All telemetry disabled.")

def disable_autoupdates() -> None:
    write_value_to_registry_key(r"HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate\AU\AutoInstallMinorUpdates", 0, winreg.REG_DWORD)
    write_value_to_registry_key(r"HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate\AU\NoAutoUpdate", 1, winreg.REG_DWORD)
    write_value_to_registry_key(r"HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\WindowsStore\AutoDownload", 2, winreg.REG_DWORD)
    write_value_to_registry_key(r"HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate\SetAutoRestartNotificationDisable", 1, winreg.REG_DWORD)
    write_value_to_registry_key(r"HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\Maps\AutoDownloadAndUpdateMapData", 0, winreg.REG_DWORD)
    
    print(" - Auto updates disabled.")

def clean_system_junk() -> None:
    for item in cleanup_keys:
        write_value_to_registry_key(item[0], item[1], item[2])
    
    run([r"cleanmgr.exe /sagerun"])
    
    temp = os.getenv('temp')
    
    for file in os.listdir(temp):
        try:
            filepath = os.path.join(temp, file)
            
            if os.path.isfile(filepath) or os.path.islink(filepath):
                os.remove(filepath)
                
            elif os.path.isdir(filepath):
                shutil.rmtree(filepath)
        except:
            continue
    
    print(" - System junk has been removed.")

def repair_corruption() -> None:
    run(["sfc /scannow"])
    
    print(" - Corrupted files have been repaired.")

def main() -> None:
    menu = """
 Options\t\t\t  Descriptions
----------------------------------------------------------------------------------
| 1: Optimize Windows\t\t| General performance and gaming optimizations \t | 
| 2: Optimize Network\t\t| Wi-Fi and Ethernet optimizations \t\t |
| 3: Disable Telemetry\t\t| Disables telemetry data collection \t\t |
| 4: Disable Auto Updates\t| Makes all updates manual \t\t\t |
| 5: Activate Windows 10/11 Pro\t| Activates Windows Pro edition for free \t |
| 6: System Cleanup\t\t| Removes junk files \t\t\t\t |
| 7: All of the above\t\t| Chooses all options \t\t\t\t |
----------------------------------------------------------------------------------
"""
    
    while(True):
        os.system("cls")
        print(menu)
        
        user_input = input("What would you like to do? [1-7]: ")
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
        elif user_input == 5: activate_win_pro()
        elif user_input == 6: clean_system_junk()
        elif user_input == 7:
            optimize_windows()
            optimize_network()
            disable_telemetry()
            disable_autoupdates()
            activate_win_pro()
            clean_system_junk()
            
        if input("\nWould you like to restart to apply changes (yes/no)? ") == "yes":
            run([r"shutdown.exe /r /t 5"])
        
if __name__ == "__main__":
    if ctypes.windll.shell32.IsUserAnAdmin() == False:
        print("I must be ran as administrator or I can't apply changes.")
        
        if input("Restart as admin (yes/no)? ") == "yes":
            run([r"Start-Process '.\WinOptimizer.exe' -Verb runAs"])
            
        sys.exit()
        
    main()