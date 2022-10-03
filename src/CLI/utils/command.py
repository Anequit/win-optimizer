from subprocess import run, DEVNULL
from rich.console import Console

def execute_command(command: str) -> None:
    if command is None:
        raise ValueError("command can't be empty")

    process = run(command, stdout=DEVNULL, stderr=DEVNULL, shell=False, capture_output=False)

    if process.returncode != 0:
        Console().print(" - Failed to run: [bold red]" + command + "[/bold red]")

def execute_commands(commands: list) -> None:
    if commands is None:
        raise ValueError("commands can't be empty")

    for command in commands:
        execute_command(command)