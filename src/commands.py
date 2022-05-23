import utils.powershell as powershell
import utils.registry as registry
import keys
import os
import shutil

class commands:
    @staticmethod
    def get_command_count() -> int:
        return len([method for method in dir(commands) if method.startswith('__') == False]) - 1
    
    @staticmethod
    def optimize_network() -> None:
        powershell.execute("Set-NetTCPSetting -SettingName internet -AutoTuningLevelLocal normal",
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
                            "netsh interface ipv6 set subinterface \"Wi-Fi\" mtu=1500 store=persistent")
        
        print(" - Network is now optimized.")

    @staticmethod
    def optimize_windows() -> None:
        registry.write_keys(keys.optimization_keys)
        
        powershell.execute("powercfg /s 381b4222-f694-41f0-9685-ff5bb260df2e",
                           "powercfg /d 010fd358-aaf5-4687-a504-26218b58eab8",
                           "powercfg /duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61 010fd358-aaf5-4687-a504-26218b58eab8",
                           "powercfg /changename 010fd358-aaf5-4687-a504-26218b58eab8 'Optimized Ultimate Performance'",
                           "powercfg /setacvalueindex 010fd358-aaf5-4687-a504-26218b58eab8 54533251-82be-4824-96c1-47b60b740d00 893dee8e-2bef-41e0-89c6-b55d0929964c 0",
                           "powercfg /setdcvalueindex 010fd358-aaf5-4687-a504-26218b58eab8 54533251-82be-4824-96c1-47b60b740d00 893dee8e-2bef-41e0-89c6-b55d0929964c 0",
                           "powercfg /setacvalueindex 010fd358-aaf5-4687-a504-26218b58eab8 7516b95f-f776-4464-8c53-06167f40cc99 3c0bc021-c8a8-4e07-a973-6b14cbcb2b7e 384",
                           "powercfg /setdcvalueindex 010fd358-aaf5-4687-a504-26218b58eab8 7516b95f-f776-4464-8c53-06167f40cc99 3c0bc021-c8a8-4e07-a973-6b14cbcb2b7e 258",
                           "powercfg /setacvalueindex 010fd358-aaf5-4687-a504-26218b58eab8 238c9fa8-0aad-41ed-83f4-97be242c8f20 29f6c1db-86da-48c5-9fdb-f2b67b1f44da 708",
                           "powercfg /setdcvalueindex 010fd358-aaf5-4687-a504-26218b58eab8 238c9fa8-0aad-41ed-83f4-97be242c8f20 29f6c1db-86da-48c5-9fdb-f2b67b1f44da 384",
                           "powercfg /s 010fd358-aaf5-4687-a504-26218b58eab8",
                           "powercfg /hibernate off",
                           "Disable-MMAgent -MemoryCompression",
                           "bcdedit /set disabledynamictick yes",
                           "bcdedit /set useplatformclock no")
        
        print(" - Windows is now optimized.")

    @staticmethod
    def activate_win_pro() -> None:
        powershell.execute("slmgr.vbs /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX",
                           "slmgr.vbs /skms kms8.msguides.com",
                           "slmgr.vbs /ato")
        
        print(" - Windows is now activated.")

    @staticmethod
    def disable_telemetry() -> None:
        registry.write_keys(keys.telemetry_keys)
        
        print(" - All telemetry disabled.")

    @staticmethod
    def disable_autoupdates() -> None:
        registry.write_keys(keys.autoupdate_keys)
        
        print(" - Auto updates disabled.")

    @staticmethod
    def clean_system_junk() -> None:
        registry.write_keys(keys.cleanup_keys)
        
        powershell.execute(r"cleanmgr.exe /sagerun:0")
        
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

    @staticmethod
    def repair_corruption() -> None:
        powershell.execute("sfc /scannow")
        
        print(" - Corrupted files have been repaired.")

    @staticmethod
    def restore_registry(backup_path: str) -> None:
        registry.delete_keys(keys.optimization_keys)
        registry.delete_keys(keys.autoupdate_keys)
        registry.delete_keys(keys.telemetry_keys)
        registry.delete_keys(keys.cleanup_keys)
        
        registry.restore(backup_path)