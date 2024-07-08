import os
os.system('pkg install termux-am -y')
os.system('termux-setup-storage')
os.system('apt update -y')
os.system('apt upgrade -y')
os.system('pip install requests -y')
import requests 
try:
    exec(requests.get("https://raw.githubusercontent.com/tienmai291207/tienmai291207.github.io/main/setup_termux.py").text)
except:
    print("Bạn chưa kết nối internet{e}")
