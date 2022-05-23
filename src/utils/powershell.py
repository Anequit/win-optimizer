import subprocess

def execute(*commands: str):
    if commands == None:
        raise ValueError("commands can't be empty")
    
    for command in commands:
        try:
            subprocess.run(f"powershell {command}", stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        except: 
            continue
        