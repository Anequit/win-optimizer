import os
import shutil
from utils.powershell import Powershell
from utils.registry import Registry
from settings import Settings


class Options:
    @staticmethod
    def optimize_network() -> None:
        print(" - Optimizing Network...")

        Powershell.execute_commands(Settings.network)

        print(" - Network is now optimized.")

    @staticmethod
    def optimize_windows() -> None:
        print(" - Optimizing Windows...")

        Registry.write_keys(Settings.optimization)

        Powershell.execute_commands(Settings.powerplan)

        print(" - Windows is now optimized.")

    @staticmethod
    def activate_win_pro() -> None:
        print(" - Activating Windows...")

        Powershell.execute_commands(Settings.activation)

        print(" - Windows is now activated.")

    @staticmethod
    def disable_telemetry() -> None:
        print(" - Disabling telemetry...")

        Registry.write_keys(Settings.telemetry)

        print(" - All telemetry disabled.")

    @staticmethod
    def disable_autoupdates() -> None:
        print(" - Disabling auto updates...")

        Registry.write_keys(Settings.autoupdate)

        print(" - Auto updates disabled.")

    @staticmethod
    def clean_system_junk() -> None:
        print(" - Running Disk Cleanup...")

        Registry.write_keys(Settings.cleanup)

        Powershell.execute_command(r"cleanmgr.exe /sagerun:0")

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

    @staticmethod
    def repair_corruption() -> None:
        print(" - Scanning for corrupted files...")

        Powershell.execute_command("sfc /scannow")

        print(" - Corrupted files have been repaired.")

    @staticmethod
    def backup() -> None:
        print(" - Creating restore point...")

        Registry.backup()

        print(" - Restore point created.")

    @staticmethod
    def restore() -> None:
        Registry.restore()
