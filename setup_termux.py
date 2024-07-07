import subprocess
import os

def mtt_setup(command):
    os.system("clear")
    print(f"Đang setup: {command}")
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError:
        pass  # Skip the error and continue with the next command

commands = [
    "apt update -y",
    "apt upgrade -y",
    "pkg install php -y",
    "pkg install python -y",
    "pkg install git -y",
    "pkg install wget -y",
    "pkg install termux-api -y",  # Install Termux API
    "pip install --upgrade pip",
    "pip install forbidden",
    "pip install requests",
    "pip install pycurl",
    "pip install bs4",
    "pip install colorama",
    "pip install pystyle",
    "pip install pyTelegramBotAPI",  # telebot module
    "pip install aiohttp"  # common module for asynchronous HTTP requests
]

for cmd in commands:
    mtt_setup(cmd)

os.system("clear")
print("\033[32mSetup successfully\nGroup 1: https://t.me/nolow_2k7\nGroup 2: https://t.me/pulfsharemodchat\nCreated by ᴍʀ ᴄs 🌷")
subprocess.run(["termux-open-url", "https://t.me/nolow_2k7"])  # Open URL using Termux API
