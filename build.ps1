pyinstaller --noconfirm --clean -D -F -i ./src/CLI/Assets/ICON.ico -n "WinOptimizer" ./src/CLI/main.py

Remove-Item -R -Force ".\build"
Remove-Item -Force "WinOptimizer.spec"
Remove-Item -R -Force ".\bin\"

Rename-Item ".\dist" ".\bin" 

Set-Location ".\bin"

Get-FileHash -A SHA256 ".\WinOptimizer.exe" | Format-List >> SHA256
Get-Content SHA256

explorer.exe .
Set-Location ..