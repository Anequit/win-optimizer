from utils.powershell import execute_commands
from os.path import isdir

def activate_windows_pro() -> None:
    execute_commands([
        r'Changepk.exe /ProductKey VK7JG-NPHTM-C97JM-9MPGT-3V66T'
        r'slmgr.vbs /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX',
        r'slmgr.vbs /skms kms8.msguides.com',
        r'slmgr.vbs /ato'
    ])

def activate_winrar() -> None:
    # check if winrar is installed
    if isdir(r"C:\Program Files\WinRAR"):
        # open key file
        file = open(r"C:\Program Files\WinRAR\rarreg.key", 'w')
        
        # write registration key to file
        file.write(("""RAR registration data\nHardik\nwww.Hardik.live\nUID=448c4a899c6cdc1039c5\n641221225039c585fc5ef8da12ccf689780883109587752a828ff0\n59ae0579fe68942c97d160f361d16f96c8fe03f1f89c66abc25a37\n7777a27ec82f103b3d8e05dcefeaa45c71675ca822242858a1c897\nc57d0b0a3fe7ac36c517b1d2be385dcc726039e5f536439a806c35\n1e180e47e6bf51febac6eaae111343d85015dbd59ba45c71675ca8\n2224285927550547c74c826eade52bbdb578741acc1565af60e326\n6b5e5eaa169647277b533e8c4ac01535547d1dee14411061928023""").strip())