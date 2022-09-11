from utils import powershell


def activate_windows_pro() -> None:
    powershell.execute_commands([
        r'Changepk.exe /ProductKey VK7JG-NPHTM-C97JM-9MPGT-3V66T'
        r'slmgr.vbs /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX',
        r'slmgr.vbs /skms kms8.msguides.com',
        r'slmgr.vbs /ato'
    ])

def activate_windows_home() -> None:
    powershell.execute_commands([
        r'Changepk.exe /ProductKey YTMG3-N6DKC-DKB77-7M9GH-8HVX7'
        r'slmgr.vbs /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX',
        r'slmgr.vbs /skms kms8.msguides.com',
        r'slmgr.vbs /ato'
    ])
    
def reset_windows_key() -> None:
    powershell.execute_command(r"Changepk.exe /ProductKey VK7JG-NPHTM-C97JM-9MPGT-3V66T")