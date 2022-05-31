import subprocess

def execute_command(command: str) -> None:
    if command == None:
        raise ValueError("command can't be empty")

    try:
        subprocess.check_call(["powershell", command], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT, shell=True)
    except:
        print("  - Failed to run: " + command)

def execute_commands(*commands: str) -> None:
    if commands == None:
        raise ValueError("commands can't be empty")
    
    for command in commands:
        execute_command(command)