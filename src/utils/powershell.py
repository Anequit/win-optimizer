import subprocess


def execute_command(command: str) -> None:
    if command is None:
        raise ValueError("command can't be empty")

    process = subprocess.call(["powershell", command], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)

    if process != 0:
        print("  - Failed to run: " + command)


def execute_commands(*commands: str) -> None:
    if commands is None:
        raise ValueError("commands can't be empty")

    for command in commands:
        execute_command(command)
