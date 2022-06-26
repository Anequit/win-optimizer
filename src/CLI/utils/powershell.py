import subprocess


class Powershell:
    @staticmethod
    def execute_command(command: str) -> None:
        if command is None:
            raise ValueError("command can't be empty")

        process = subprocess.run(["powershell", command], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True, capture_output=False)

        if process.returncode != 0:
            print("  - Failed to run: " + command)

    @staticmethod
    def execute_commands(commands: list) -> None:
        if commands is None:
            raise ValueError("commands can't be empty")

        for command in commands:
            Powershell.execute_command(command)
