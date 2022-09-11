import subprocess


def execute_command(command: str) -> None:
    if command is None:
        raise ValueError("command can't be empty")

    process = subprocess.run(f"powershell {command}", stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True, capture_output=False)

    if process.returncode != 0:
        print("  - Failed to run: " + command)

def execute_commands(commands: list) -> None:
    if commands is None:
        raise ValueError("commands can't be empty")

    for command in commands:
        execute_command(command)