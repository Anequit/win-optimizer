from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import IntPrompt
from rich import box

import os

menu_options = [["General Optimizations", "General performance and gaming optimizations", [
                 ["Telemetry", "Disables Windows telemetry", "Yes"],
                 ["Services", "Disables unnecessary services that slow down startup", "Yes"],
                 ["Responsiveness", "Improve system responsiveness", "Yes"],
                 ["Auto Update", "Disabled Windows auto update", "Yes"],
                 ["Powerplan", "Installs optimized ultimate powerplan", "Yes"]]],
                ["Network Optimizations", "Wi-Fi and Ethernet optimizations", [
                 ["DNS", "Set DNS to Cloudflare and Google DNS servers", "No"],
                 ["Services", "Configure network services", "No"],
                 ["Throttling", "Disable network throttling", "No"],
                 ["Adapter", "Configure network adapter", "No"]]],
                ["Windows Activation", "Windows key reset and activation", [
                 ["Reset Key", "Switches to Windows generic key", "No"],
                 ["Windows Pro", "Activates Windows Pro edition", "No"],
                 ["Windows Home", "Activates Windows Home edition", "No"]]]]

def display_sections() -> None:
    table = Table(box=box.MINIMAL)
    
    table.padding = (0, 2, 0, 2)
    
    table.add_column("Sections", justify="left")
    table.add_column("Descriptions", justify="left")
    
    for item in range(len(menu_options)):
        table.add_row(f"{item + 1}: {menu_options[item][0]}", menu_options[item][1])
    
    table.add_row(f"{len(menu_options) + 1}: Quit", "Exit application")
    
    Console().print(Panel(title="Home", title_align="left", renderable=table, padding=(0, 0), highlight=True, expand=False))

def display_options(section: list) -> None:
    table = Table(box=box.MINIMAL)
    
    table.padding = (0, 2, 0, 2)
    
    table.add_column("Options", justify="left")
    table.add_column("Descriptions", justify="left")
    table.add_column("Reversible", justify="center")
        
    for item in range(len(section[2])):
        table.add_row(f"{item + 1}: {section[2][item][0]}", section[2][item][1], section[2][item][2])
    
    table.add_row(f"{len(section[2]) + 1}: Home", "Returns to home page")
    
    Console().print(Panel(title=section[0], title_align="left", renderable=table, padding=(0, 0), highlight=True, expand=False))

def get_section_input() -> int:
    "Prompt user to enter a value"
    
    sectionsLength = len(menu_options) + 1 # Add 1 to account for quit option
    
    while True:
        result = IntPrompt.ask(f"Which [b]section[/b] would you like to visit? [1-{sectionsLength}]")
        
        if(result >= 1 and result <= sectionsLength):
            return result
        
        Console().print(f"[prompt.invalid]Section must be between 1 and {sectionsLength}")

def get_option_input(section: int) -> int:
    "Prompt user to enter a value"
    
    sectionLength = len(menu_options[section][2]) + 1 # Add 1 to account for home option
    
    while True:
        result = IntPrompt.ask(f"Which [b]option[/b] would you like to do? [1-{sectionLength}]")
        
        if(result >= 1 and result <= sectionLength):
            return result
        
        Console().print(f"[prompt.invalid]Option must be between 1 and {sectionLength}")
    
def resolve_option(section: int, option: int) -> None:
    "Evaluate which option was selected"
    pass

def clear_screen() -> None:
    os.system("cls")