from os import system

from rich import box
from rich.console import Console
from rich.panel import Panel
from rich.prompt import IntPrompt
from rich.table import Table

from options.general_optimizations import *
from options.network_optimizations import *
from options.registry import *
from utils.command import *

menu_options = [
    ["General Optimizations", "General performance and gaming optimizations", [
        ["Telemetry", "Disables Windows telemetry", True, disable_telemetry],
        ["Services", "Disables unnecessary services that slow down startup", True, improve_startup],
        ["Responsiveness", "Improve system responsiveness", True, improve_responsiveness],
        ["Auto Update", "Disabled Windows auto update", True, disable_autoupdate],
        ["Powerplan", "Installs optimized ultimate powerplan", True, install_powerplan]]],
    ["Network Optimizations", "Wi-Fi and Ethernet optimizations", [
        ["DNS", "Set DNS to Cloudflare and Google DNS servers", False, update_dns],
        ["Services", "Configure network services", False, disable_services],
        ["Throttling", "Disable network throttling", False, disable_throttling],
        ["Adapter", "Configure network adapter", False, configure_adapter]]],
    ["Software Activation", "Activate software and Windows", [
        ["Activate Windows", "Activates Windows Pro edition", False, activate_windows_pro],
        ["Activate WinRAR", "Activates Windows Home edition", False, activate_winrar]]],
    ["Registry", "Options for restoring or backing up registry", [
        ["Restore", "Opens recovery control panel", False, restore_registry],
        ["Backup", "Backs up registry", True, backup_registry]]]
]


def display_title() -> None:
    Console().print(r""" 
 ██╗    ██╗██╗███╗   ██╗       ██████╗ ██████╗ ████████╗██╗███╗   ███╗██╗███████╗███████╗██████╗ 
 ██║    ██║██║████╗  ██║      ██╔═══██╗██╔══██╗╚══██╔══╝██║████╗ ████║██║╚══███╔╝██╔════╝██╔══██╗
 ██║ █╗ ██║██║██╔██╗ ██║█████╗██║   ██║██████╔╝   ██║   ██║██╔████╔██║██║  ███╔╝ █████╗  ██████╔╝
 ██║███╗██║██║██║╚██╗██║╚════╝██║   ██║██╔═══╝    ██║   ██║██║╚██╔╝██║██║ ███╔╝  ██╔══╝  ██╔══██╗
 ╚███╔███╔╝██║██║ ╚████║      ╚██████╔╝██║        ██║   ██║██║ ╚═╝ ██║██║███████╗███████╗██║  ██║
  ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝       ╚═════╝ ╚═╝        ╚═╝   ╚═╝╚═╝     ╚═╝╚═╝╚══════╝╚══════╝╚═╝  ╚═╝                                               
          """, highlight=True, markup=True, justify="center")


def display_sections() -> None:
    table = Table(box=box.MINIMAL, expand=True)

    table.padding = (0, 2, 0, 2)

    table.add_column("Sections", justify="left")
    table.add_column("Descriptions", justify="left")

    for item in range(len(menu_options)):
        table.add_row(f"{item + 1}: {menu_options[item][0]}", menu_options[item][1])

    table.add_row(f"{len(menu_options) + 1}: Quit", "Exit application")

    Console().print(Panel(title="Home", title_align="left", renderable=table, padding=(0, 0), highlight=True))
    Console().print("")


def display_options(section: list) -> None:
    table = Table(box=box.MINIMAL, expand=True)

    table.padding = (0, 2, 0, 2)

    table.add_column("Options", justify="left")
    table.add_column("Descriptions", justify="left")
    table.add_column("Reversible", justify="center")

    for item in range(len(section[2])):
        reversible = section[2][item][2]

        if reversible:
            reversible = f"[bold green]Yes[/bold green]"

        else:
            reversible = f"[bold red]No[/bold red]"

        table.add_row(f"{item + 1}: {section[2][item][0]}", section[2][item][1], reversible)

    table.add_row(f"{len(section[2]) + 1}: Home", "Returns to home page")

    Console().print(Panel(title=section[0], title_align="left", renderable=table, padding=(0, 0), highlight=True))
    Console().print("")


def get_section_input() -> int:
    """Prompt user to enter a value"""

    section_length = len(menu_options) + 1  # Add 1 to account for quit option

    while True:
        result = IntPrompt.ask(f"Which [b]section[/b] would you like to visit? [1-{section_length}]")

        if 1 <= result <= section_length:
            return result

        Console().print(f"[prompt.invalid]Section must be between 1 and {section_length}")


def get_option_input(section: int) -> int:
    """Prompt user to enter a value"""

    section_length = len(menu_options[section][2]) + 1  # Add 1 to account for home option

    while True:
        result = IntPrompt.ask(f"Which [b]option[/b] would you like to do? [1-{section_length}]")

        if 1 <= result <= section_length:
            return result

        Console().print(f"[prompt.invalid]Option must be between 1 and {section_length}")


def resolve_option(section: int, option: int) -> None:
    """Evaluate which option was selected"""

    menu_options[section][2][option][3]()


def restart() -> None:
    result = Confirm.ask("Would you like to restart? ", default=True, show_default=True)

    if result:
        execute_command("shutdown -r -t 5")


def clear_screen() -> None:
    system("cls")
