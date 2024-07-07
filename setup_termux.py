import subprocess
import os
import time

def mtt_setup(command):
    os.system("clear")
    print(f"\033[93mĐang setup: {command}\033[0m")
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError:
        pass  

# Lấy thông tin IP
ip = subprocess.check_output(['curl', '-s', 'https://api.ipify.org']).decode('utf-8').strip()

# Lấy thông tin quốc gia từ IP
country = subprocess.check_output(['curl', '-s', 'https://ipapi.co/{}/country_name/'.format(ip)]).decode('utf-8').strip()

# Lấy thông tin RAM, ổ đĩa, hệ điều hành và mô hình
ram = subprocess.check_output(['free', '-h']).decode('utf-8').strip()
disk = subprocess.check_output(['df', '-h']).decode('utf-8').strip()
os_info = subprocess.check_output(['uname', '-a']).decode('utf-8').strip()
model_name = subprocess.check_output(['getprop', 'ro.product.model']).decode('utf-8').strip()
device_name = subprocess.check_output(['getprop', 'ro.product.device']).decode('utf-8').strip()

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
print(f"Tổng thời gian: {elapsed_time:.2f} giây")
print(f"IP: {ip}")
print(f"Quốc gia: {country}")
print("Thông tin hệ thống:")
print(f"RAM:\n{ram}")
print(f"Ổ đĩa:\n{disk}")
print(f"Hệ điều hành: {os_info}")
print(f"Mô hình thiết bị: {model_name}")
print(f"Tên thiết bị: {device_name}")
print("Group 1: https://t.me/nolow_2k7")
print("Group 2: https://t.me/pulfsharemodchat")
print("Created by ᴍʀ ᴄs 🌷")
subprocess.run(["termux-open-url", "https://t.me/nolow_2k7"])
