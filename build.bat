pyinstaller --noconfirm --clean -D -F -i ./src/Assets/ICON.ico -n "WinOptimizer" ./src/main.py

cd dist
explorer.exe .