import subprocess
import os
import time
import socket
import platform

def mtt_ip():
    try:
        ip = socket.gethostbyname(socket.gethostname())
    except:
        ip = "Không lấy được IP"
    return ip
def mtt_model():
    try:
        model = platform.machine()
    except:
        model = "Không lấy được model"
    return model
def mtt_setup(command):
    os.system("clear")
    print(f"\033[93mĐang setup: {command}\033[0m")
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError:
        pass  

commands = [
    "apt update -y",
    "apt upgrade -y",
    "pkg install php -y",
    "pkg install python3 -y",
    "pkg install git -y",
    "pkg install wget -y",
    "pkg install termux-api -y",
    "pip install telebot",
    "pip install requests",
    "pip install pycurl",
    "pip install bs4",
    "pip install colorama",
    "pip install pystyle",
    "pip install pyTelegramBotAPI", 
    "pip install aiohttp"
]

start_time = time.time()
for cmd in commands:
    mtt_setup(cmd)
end_time = time.time()
elapsed_time = end_time - start_time
os.system("clear")
print("\033[32mSetup thành công!")
print(f"\033[37mThời gian setup: {elapsed_time:.2f} giây")
print(f"IP: {mtt_ip()}")
print(f"Model: {mtt_model()}")
print("Group 1: https://t.me/nolow_2k7")
print("Group 2: https://t.me/pulfsharemodchat")
print("Created by ᴍʀ ᴄs 🌷")
subprocess.run(["termux-open-url", "https://t.me/nolow_2k7"])
