import json
import os
import time
import utils.helper as helper
from function import (
    login
)

DATA_FILE = 'tips_belajar.json'

def load_tips_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return{}

def save_tips_data(tips_data):
    with open(DATA_FILE, 'w') as file:
        json.dump(tips_data, file, indent=4)

def tambahTips():
    admin = input("Masukkan nama anda: ")
    tips = input("Masukkan Tips: ")
    
    tips_data = load_tips_data()

    if tips in tips_data:
        print("\nTips sudah ada! Silakan masukkan tips kembali.")
        time.sleep(1)
        return
    
    tips_data[admin] = tips
    save_tips_data(tips_data)
    print("Berhasil menyimpan tips. ") 

def main(username):
    """Main function to run the CLI login system."""
    while True:
        helper.clear()
        print(f"Silahkan {username} memilih option!\n")
        print("1. Tambah tips")
        print("2. exit")
        choice = input("Pilih dengan angka: ")

        if choice == '1':
            helper.clear()
            tambahTips()
        elif choice == '2':
            login.main()
            break
        else:
            print("\nInvalid input! Silakan coba lagi.")
            time.sleep(1)

