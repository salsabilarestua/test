import json
import os
import getpass
import time
import utils.helper as helper

DATA_FILE = 'user_data.json'

def load_user_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return {}

def save_user_data(user_data):
    with open(DATA_FILE, 'w') as file:
        json.dump(user_data, file, indent=4)

def register():
    username = input("Masukkan username: ")
    password = getpass.getpass("Masukkan password baru: ")
    
    user_data = load_user_data()
    
    if username in user_data:
        print("\nUsername sudah ada! Silakan coba login kembali.")
        time.sleep(1)
        return
    
    user_data[username] = password
    save_user_data(user_data)
    print("Berhasil Register.")

def login():
    username = input("Masukkan username: ")
    password = getpass.getpass("Masukkan password: ")

    user_data = load_user_data()
    
    if username in user_data and user_data[username] == password:
        print("\nLogin Berhasil!")
        time.sleep(1)
        return True, username # Jika berhasil login return True agar bisa dilakukan check
    else:
        print("\nUsername atau Password salah!")
        time.sleep(1)
        return False, None # Jika login salah return False

def main():
    """Main function to run the CLI login system."""
    while True:
        helper.clear()
        print("Silahkan melakukan login terlebih dahulu!\n")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Pilih dengan angka: ")

        if choice == '1':
            helper.clear()
            register()
        elif choice == '2':
            helper.clear()
            result, user = login()
            if result:
                helper.clear()
                return user
        elif choice == '3':
            break
        else:
            print("\nInvalid input! Silakan coba lagi.")
            time.sleep(1)
