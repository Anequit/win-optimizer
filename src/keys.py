import winreg

optimization_keys = [(r"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\AxInstSV\Start", 4, winreg.REG_DWORD),
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
                     (r"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Tcpip\ServiceProvider\LocalPriority", 4, winreg.REG_DWORD),
                     (r"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Tcpip\ServiceProvider\HostsPriority", 5, winreg.REG_DWORD),
                     (r"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Tcpip\ServiceProvider\DnsPriority", 6, winreg.REG_DWORD),
                     (r"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Tcpip\ServiceProvider\NetbtPriority", 7, winreg.REG_DWORD),
                     (r"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Tcpip\QoS\Do not use NLA", "1", winreg.REG_SZ),
                     (r"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\LanmanServer\Parameters\Size", 3, winreg.REG_DWORD),
                     (r"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\MaxUserPort", 65534, winreg.REG_DWORD),
                     (r"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\TcpTimedWaitDelay", 30, winreg.REG_DWORD),
                     (r"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\DefaultTTL", 64, winreg.REG_DWORD),
                     (r"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Power\PowerThrottling\PowerThrottlingOff", 1, winreg.REG_DWORD),
                     (r"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\FileSystem\NtfsDisable8dot3NameCreation", 1, winreg.REG_DWORD),
                     (r"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management\LargeSystemCache", 1, winreg.REG_DWORD),
                     (r"HKEY_CURRENT_USER\Control Panel\Desktop\HungAppTimeout", "4000", winreg.REG_SZ),
                     (r"HKEY_CURRENT_USER\Control Panel\Desktop\WaitToKillAppTimeout", "5000", winreg.REG_SZ),
                     (r"HKEY_CURRENT_USER\Control Panel\Desktop\MenuShowDelay", "0", winreg.REG_SZ),
                     (r"HKEY_CURRENT_USER\Control Panel\Desktop\ForegroundLockTimeout", 200000, winreg.REG_DWORD),
                     (r"HKEY_CURRENT_USER\Control Panel\Desktop\AutoEndTasks", "1", winreg.REG_SZ),
                     (r"HKEY_CURRENT_USER\Control Panel\Mouse\MouseHoverTime", "100", winreg.REG_SZ),
                     (r"HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\BackgroundAccessApplications\GlobalUserDisabled", 1, winreg.REG_DWORD),
                     (r"HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\DesktopProcess", 1, winreg.REG_DWORD),
                     (r"HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\GameDVR\AppCaptureEnabled", 0, winreg.REG_DWORD),
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
                     (r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Internet Explorer\Main\FeatureControl\FEATURE_MAXCONNECTIONSPERSERVER\explorer.exe", 10, winreg.REG_DWORD),
                     (r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Internet Explorer\Main\FeatureControl\FEATURE_MAXCONNECTIONSPER1_0SERVER\explorer.exe", 10, winreg.REG_DWORD),
                     (r"HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\Psched\NonBestEffortLimit", 0, winreg.REG_DWORD),
                     (r"HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\Psched\TimerResolution", 0, winreg.REG_DWORD),
                     (r"HKEY_CURRENT_USER\System\GameConfigStore\GameDVR_Enabled", 0, winreg.REG_DWORD),
                     (r"HKEY_CURRENT_USER\System\GameConfigStore\GameDVR_FSEBehavior", 2, winreg.REG_DWORD)]

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

telemetry_keys = [(r"HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\DataCollection\AllowTelemetry", 0, winreg.REG_DWORD),
                  (r"HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\TabletPC\PreventHandwritingDataSharing", 1, winreg.REG_DWORD),
                  (r"HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\Psched\NonBestEffortLimit", 0, winreg.REG_DWORD),
                  (r"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\DiagTrack\Start", 4, winreg.REG_DWORD),
                  (r"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\dmwappushservice\Start", 4, winreg.REG_DWORD),
                  (r"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\diagsvc\Start", 4, winreg.REG_DWORD),
                  (r"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\diagnosticshub.standardcollector.service\Start", 4, winreg.REG_DWORD)]

autoupdate_keys = [(r"HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate\AU\AutoInstallMinorUpdates", 0, winreg.REG_DWORD),
                   (r"HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate\AU\NoAutoUpdate", 1, winreg.REG_DWORD),
                   (r"HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\WindowsStore\AutoDownload", 2, winreg.REG_DWORD),
                   (r"HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate\SetAutoRestartNotificationDisable", 1, winreg.REG_DWORD),
                   (r"HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\Maps\AutoDownloadAndUpdateMapData", 0, winreg.REG_DWORD)]
