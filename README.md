# windows-setup-tool
[![GitHub all releases](https://img.shields.io:/github/downloads/Anequit/windows-setup-tool/total)](https://github.com/Anequit/SCD/releases)
[![GitHub release (latest by date)](https://img.shields.io:/github/v/release/Anequit/windows-setup-tool)](https://github.com/Anequit/SCD/releases)
[![GitHub repo size](https://img.shields.io:/github/repo-size/Anequit/windows-setup-tool)](https://github.com/Anequit/SCD/releases)


## About
This tool was made to make my life a little easier when I have to reinstall my OS for the 900th time. It's build specifically for myself, but you can tweak it or adjust it how you'd like. 


## What does this do?
This tool optimizes windows to it's fullest potential for gaming, disables windows telemetry and data collection, disables auto updating and disables the update restart prompt. It also optimizes the network configuration behind the scenes to give you more bandwidth in gaming. This tool can also install a suite of software for you, so you don't have to spend 20 minutes downloading and installing from 15 different websites. Finally, it also activates windows 10/11 pro, so you don't need to deal with the limitations of home edition.


## What if I don't like the software it installs?
You can override the defaults by following the the short guide below.

1. Create a `software.txt` file in the same directory as the tool.
2. Open a terminal and search for the software you want to include with `winget search <name>`
3. Copy and paste either the id or the name into `software.txt`
4. Reopen the tool it will now use the software listed in `software.txt` instead of the defaults.

*Note: If the software you want to include has a duplicate name in winget, then use the id instead.*
