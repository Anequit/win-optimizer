pyinstaller --noconfirm --clean -F --uac-admin -i ./src/CLI/Assets/ICON.ico -n "win-optimizer" ./src/CLI/main.py

Remove-Item -R -Force ".\build"
Remove-Item -Force "win-optimizer.spec"
Remove-Item -R -Force ".\bin\"

Rename-Item ".\dist" ".\bin" 

Set-Location ".\bin"

Get-FileHash -A SHA256 ".\win-optimizer.exe"

explorer.exe .
Set-Location ..