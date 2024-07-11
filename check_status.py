import requests

status_url = 'https://anotepad.com/notes/xegjwyky'

def check_status():
    try:
        response = requests.get(status_url)
        if response.text.strip() == "Trừng Phạt ON":
            return True
        else:
            print("\033[1;31mTool is currently OFF. Exiting.")
            return False
    except Exception as e:
        print(f"\033[1;31mError checking status: {e}")
        return False

if __name__ == "__main__":
    if check_status():
        print("\033[1;32mTool is active. Proceed with operations.")
    else:
        print("\033[1;31mTool is not active. Exiting.")

