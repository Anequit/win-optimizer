# win-optimizer
[![GitHub all releases](https://img.shields.io:/github/downloads/Anequit/win-optimizer/total)](https://github.com/Anequit/win-optimizer/releases)
[![GitHub release (latest by date)](https://img.shields.io:/github/v/release/Anequit/win-optimizer)](https://github.com/Anequit/win-optimizer/releases)
[![GitHub repo size](https://img.shields.io:/github/repo-size/Anequit/win-optimizer)](https://github.com/Anequit/win-optimizer/releases)


## About
This tool was made to make my life a little easier when I have to reinstall my OS for the 900th time, but anyone can use it.


## What does this do?
This tool optimizes windows to it's fullest potential, disables telemetry/data collection, disables auto updating, and activates windows for you. The tweaks made by this tool will increase overall system performance, framerate in games, and network performance, but will also cause windows to draw more power. Due to this extra power draw, this tool may not be ideal for laptops with a working battery.


## Flagged as virus?
Due to how this program writes changes to Windows it's flagged as a virus. If that worries you, then you can compile the binary yourself with the guide below.

1. Download the [latest version](https://www.python.org/downloads/) of Python.

2. Clone the repository or download as zip and extract it. If you don't know how to do that then [here](https://www.youtube.com/watch?v=X5e3xQBeqf8) is a tutorial.

3. Navigate to the repository and run `pip install -r requirements.txt` in the terminal. If you've never used the terminal then [here](https://wiki.communitydata.science/Windows_terminal_navigation) is a simple article on how to use it.

4. Now you'll need to enable scripts, so you can run the build script. In powershell, run `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Bypass -Force` and then continue to the next step. 

5. Now, you can run `build.ps1` in terminal or by right clicking and running with powershell.

6. You should now see your brand new binary waiting for you to run it!

## Windows activation isn't working
Steps to resolve this problem are located in this [issue](https://github.com/Anequit/win-optimizer/issues/10), I am still investigating it and may release a patch fixing it in the future.

## What is file integrity?
File integrity allows you to verify that the file you downloaded is identical the one uploaded. In the release, there will be a couple hashes you can use to verify the integrity of the binary. 

1. Start by downloading the latest version [here](https://github.com/Anequit/win-optimizer/releases/latest), then copy and save the SHA256 hash.

2. Open powershell and navigate to the directory where `WinOptimizer.exe` is located.

3. Run the command `Get-FileHash .\WinOptimizer.exe`.

4. Compare the hash listed with the hash from the release page.

5. If they match, then the files are identical.
