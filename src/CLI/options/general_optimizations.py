from utils.powershell import execute_commands


def disable_telemetry() -> None:
    execute_commands([
        r'reg add HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\DataCollection /v AllowTelemetry /t REG_DWORD /d 0 /f',
        r'reg add HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\TabletPC /v PreventHandwritingDataSharing /t REG_DWORD /d 1 /f',
        r'reg add HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\DiagTrack /v Start /t REG_DWORD /d 4 /f',
        r'reg add HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\diagsvc /v Start /t REG_DWORD /d 4 /f',
        r'reg add HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\diagnosticshub.standardcollector.service /v Start /t REG_DWORD /d 4 /f',
        r'reg add HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Privacy /v TailoredExperiencesWithDiagnosticDataEnabled /t REG_DWORD /d 0 /f'
    ])

def improve_startup() -> None:
    execute_commands([
        r'reg add HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\AxInstSV /v Start /t REG_DWORD /d 3 /f',
        r'reg add HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\AppMgmt /v Start /t REG_DWORD /d 3 /f',
        r'reg add HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\CertPropSvc /v Start /t REG_DWORD /d 3 /f',
        r'reg add HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\PeerDistSvc /v Start /t REG_DWORD /d 3 /f',
        r'reg add HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\SCPolicySvc /v Start /t REG_DWORD /d 3 /f',
        r'reg add HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\SNMPTRAP /v Start /t REG_DWORD /d 3 /f',
        r'reg add HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\WebClient /v Start /t REG_DWORD /d 3 /f',
        r'reg add HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\WinRM /v Start /t REG_DWORD /d 3 /f',
        r'reg add HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\WerSvc /v Start /t REG_DWORD /d 3 /f',
        r'reg add HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\PNRPsvc /v Start /t REG_DWORD /d 3 /f',
        r'reg add HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\p2psvc /v Start /t REG_DWORD /d 3 /f',
        r'reg add HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\p2pimsvc /v Start /t REG_DWORD /d 3 /f',
        r'reg add HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\SysMain /v DelayedAutoStart /t REG_DWORD /d 1 /f',
        r'reg add HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\"Session Manager"\Power /v HiberbootEnabled /t REG_DWORD /d 0 /f'
    ])

def improve_responsiveness() -> None:
    execute_commands([
        r'reg add HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\BackgroundAccessApplications /v GlobalUserDisabled /t REG_DWORD /d 1 /f',
        r'reg add HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer /v DesktopProcess /t REG_DWORD /d 1 /f',
        r'reg add HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Dfrg\BootOptimizeFunction /v Enable /t REG_SZ /d Y /f',
        r'reg add HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer /v "Max Cached Icons" /t REG_DWORD /d 2000 /f',
        r'reg add HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\"Windows NT"\CurrentVersion\Multimedia\SystemProfile /v SystemResponsiveness /t REG_DWORD /d 0 /f',
        r'bcdedit /set disabledynamictick yes',
        r'bcdedit /set useplatformclock no',
        r'reg add HKEY_CURRENT_USER\"Control Panel"\Desktop /v HungAppTimeout /t REG_SZ /d 4000 /f',
        r'reg add HKEY_CURRENT_USER\"Control Panel"\Desktop /v WaitToKillAppTimeout /t REG_SZ /d 5000 /f',
        r'reg add HKEY_CURRENT_USER\"Control Panel"\Desktop /v MenuShowDelay /t REG_SZ /d 0 /f',
        r'reg add HKEY_CURRENT_USER\"Control Panel"\Desktop /v ForegroundLockTimeout /t REG_DWORD /d 200000 /f',
        r'reg add HKEY_CURRENT_USER\"Control Panel"\Desktop /v AutoEndTasks /t REG_SZ /d 1 /f',
        r'reg add HKEY_CURRENT_USER\"Control Panel"\Mouse /v MouseHoverTime /t REG_SZ /d 100 /f',
        r'reg add HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\GameDVR /v AppCaptureEnabled /t REG_DWORD /d 0 /f',
        r'reg add HKEY_CURRENT_USER\System\GameConfigStore /v GameDVR_Enabled /t REG_DWORD /d 0 /f',
        r'reg add HKEY_CURRENT_USER\System\GameConfigStore /v GameDVR_FSEBehavior /t REG_DWORD /d 2 /f',
        r'reg add HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\"Windows NT"\CurrentVersion\Multimedia\SystemProfile\Tasks\Games /v Affinity /t REG_DWORD /d 0 /f',
        r'reg add HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\"Windows NT"\CurrentVersion\Multimedia\SystemProfile\Tasks\Games /v "Background Only" /t REG_SZ /d False /f',
        r'reg add HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\"Windows NT"\CurrentVersion\Multimedia\SystemProfile\Tasks\Games /v "Clock Rate" /t REG_DWORD /d 10000 /f',
        r'reg add HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\"Windows NT"\CurrentVersion\Multimedia\SystemProfile\Tasks\Games /v "GPU Priority" /t REG_DWORD /d 8 /f',
        r'reg add HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\"Windows NT"\CurrentVersion\Multimedia\SystemProfile\Tasks\Games /v Priority /t REG_DWORD /d 6 /f',
        r'reg add HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\"Windows NT"\CurrentVersion\Multimedia\SystemProfile\Tasks\Games /v "Scheduling Category" /t REG_SZ /d High /f',
        r'reg add HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\"Windows NT"\CurrentVersion\Multimedia\SystemProfile\Tasks\Games /v "SFIO Priority" /t REG_SZ /d High /f',
        r'reg add HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Power\PowerThrottling /v PowerThrottlingOff /t REG_DWORD /d 1 /f',
        r'Disable-MMAgent -MemoryCompression',
        r'reg add HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\"Session Manager"\"Memory Management"\ /v LargeSystemCache /t REG_DWORD /d 1 /f'
    ])

def disable_autoupdate() -> None:
    execute_commands([
        r'reg add HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate\AU /v AutoInstallMinorUpdates /t REG_DWORD /d 0 /f',
        r'reg add HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate\AU /v NoAutoUpdate /t REG_DWORD /d 1 /f',
        r'reg add HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\WindowsStore /v AutoDownload /t REG_DWORD /d 2 /f',
        r'reg add HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate /v SetAutoRestartNotificationDisable /t REG_DWORD /d 1 /f',
        r'reg add HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\Maps /v AutoDownloadAndUpdateMapData /t REG_DWORD /d 0 /f'
    ])

def install_powerplan() -> None:
    execute_commands([
        r'powercfg /s 381b4222-f694-41f0-9685-ff5bb260df2e',
        r'powercfg /d 010fd358-aaf5-4687-a504-26218b58eab8',
        r'powercfg /duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61 010fd358-aaf5-4687-a504-26218b58eab8',
        r'powercfg /changename 010fd358-aaf5-4687-a504-26218b58eab8 "Optimized Ultimate Performance"',
        r'powercfg /setacvalueindex 010fd358-aaf5-4687-a504-26218b58eab8 54533251-82be-4824-96c1-47b60b740d00 893dee8e-2bef-41e0-89c6-b55d0929964c 0',
        r'powercfg /setdcvalueindex 010fd358-aaf5-4687-a504-26218b58eab8 54533251-82be-4824-96c1-47b60b740d00 893dee8e-2bef-41e0-89c6-b55d0929964c 0',
        r'powercfg /setacvalueindex 010fd358-aaf5-4687-a504-26218b58eab8 7516b95f-f776-4464-8c53-06167f40cc99 3c0bc021-c8a8-4e07-a973-6b14cbcb2b7e 900',
        r'powercfg /setdcvalueindex 010fd358-aaf5-4687-a504-26218b58eab8 7516b95f-f776-4464-8c53-06167f40cc99 3c0bc021-c8a8-4e07-a973-6b14cbcb2b7e 600',
        r'powercfg /setacvalueindex 010fd358-aaf5-4687-a504-26218b58eab8 238c9fa8-0aad-41ed-83f4-97be242c8f20 29f6c1db-86da-48c5-9fdb-f2b67b1f44da 1800',
        r'powercfg /setdcvalueindex 010fd358-aaf5-4687-a504-26218b58eab8 238c9fa8-0aad-41ed-83f4-97be242c8f20 29f6c1db-86da-48c5-9fdb-f2b67b1f44da 900',
        r'powercfg /setacvalueindex 010fd358-aaf5-4687-a504-26218b58eab8 238c9fa8-0aad-41ed-83f4-97be242c8f20 94ac6d29-73ce-41a6-809f-6363ba21b47e 0',
        r'powercfg /setdcvalueindex 010fd358-aaf5-4687-a504-26218b58eab8 238c9fa8-0aad-41ed-83f4-97be242c8f20 94ac6d29-73ce-41a6-809f-6363ba21b47e 0',
        r'powercfg /setacvalueindex 010fd358-aaf5-4687-a504-26218b58eab8 19cbb8fa-5279-450e-9fac-8a3d5fedd0c1 12bbebe6-58d6-4636-95bb-3217ef867c1a 0',
        r'powercfg /setdcvalueindex 010fd358-aaf5-4687-a504-26218b58eab8 19cbb8fa-5279-450e-9fac-8a3d5fedd0c1 12bbebe6-58d6-4636-95bb-3217ef867c1a 3',
        r'powercfg /setacvalueindex 010fd358-aaf5-4687-a504-26218b58eab8 2a737441-1930-4402-8d77-b2bebba308a3 48e6b7a6-50f5-4782-a5d4-53bb8f07e226 1',
        r'powercfg /setdcvalueindex 010fd358-aaf5-4687-a504-26218b58eab8 2a737441-1930-4402-8d77-b2bebba308a3 48e6b7a6-50f5-4782-a5d4-53bb8f07e226 1',
        r'powercfg /setacvalueindex 010fd358-aaf5-4687-a504-26218b58eab8 501a4d13-42af-4429-9fd1-a8218c268e20 ee12f906-d277-404b-b6da-e5fa1a576df5 0',
        r'powercfg /setdcvalueindex 010fd358-aaf5-4687-a504-26218b58eab8 501a4d13-42af-4429-9fd1-a8218c268e20 ee12f906-d277-404b-b6da-e5fa1a576df5 2',
        r'powercfg /setacvalueindex 010fd358-aaf5-4687-a504-26218b58eab8 9596fb26-9850-41fd-ac3e-f7c3c00afd4b 10778347-1370-4ee0-8bbd-33bdacaade49 1',
        r'powercfg /setdcvalueindex 010fd358-aaf5-4687-a504-26218b58eab8 9596fb26-9850-41fd-ac3e-f7c3c00afd4b 10778347-1370-4ee0-8bbd-33bdacaade49 0',
        r'powercfg /setacvalueindex 010fd358-aaf5-4687-a504-26218b58eab8 9596fb26-9850-41fd-ac3e-f7c3c00afd4b 34c7b99f-9a6d-4b3c-8dc7-b6693b78cef4 0',
        r'powercfg /setdcvalueindex 010fd358-aaf5-4687-a504-26218b58eab8 9596fb26-9850-41fd-ac3e-f7c3c00afd4b 34c7b99f-9a6d-4b3c-8dc7-b6693b78cef4 2',
        r'powercfg /s 010fd358-aaf5-4687-a504-26218b58eab8',
        r'powercfg /hibernate off'
    ])