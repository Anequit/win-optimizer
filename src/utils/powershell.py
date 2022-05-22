import subprocess

def execute(*commands: str):
    if commands == None:
        raise ValueError("commands can't be empty")
    
    for command in commands:
        try:
            subprocess.run(f"powershell [void]({command})", shell=True)
        except: 
            continue
        