pyinstaller --noconfirm --clean -D -F -i ./src/Assets/ICON.ico -n "WST" ./src/main.py

cd dist
explorer.exe .