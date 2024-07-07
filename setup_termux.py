import subprocess
import os
def mtt_setup(command):
    try:
        subprocess.run(command, shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except subprocess.CalledProcessError as e:
        print(f"Lỗi rồi")
        
commands = [
    "pkg install termux-am -y",
    "termux-setup-storage",
    "apt update -y && apt upgrade -y",
    "pkg install php -y",
    "pkg install python -y",
    "pkg install git -y",
    "pkg install wget -y",
    "pip install --upgrade pip",
    "pip install forbidden",
    "pip install requests",
    "pip install pycurl bs4 colorama pystyle"
]

for cmd in commands:
    mtt_setup(cmd)
os.system("clear")
print("\033[32mSetup successfully\nGroup 1: https://t.me/nolow_2k7/nGroup 2: https://t.me/pulfsharemodchat/nCreated by ᴍʀ ᴄs 🌷")
