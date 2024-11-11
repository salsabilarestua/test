import json
import os
import getpass


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
        print("Username sudah ada. Silakan coba login.")
        return

    
    user_data[username] = password
    save_user_data(user_data)
    print("Berhasil Register.")

def login():
    
    username = input("Masukkan username: ")
    password = getpass.getpass("Masukkan password: ")

    
    user_data = load_user_data()
    
    if username in user_data and user_data[username] == password:
        print("Login Berhasil!")
        return True # Jika berhasil login return True agar bisa dilakukan check
    else:
        print("Username atau Password salah!")
        return False # Jika login salah return False

def main():
    """Main function to run the CLI login system."""
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Pilih dengan angka: ")

        if choice == '1':
            register()
        elif choice == '2':
            if login():
                break # Keluar dari menu login jika login berhasil
        elif choice == '3':
            break
        else:
            print("Salah input. Silakan coba lagi.")

if __name__ == "__main__":
    main()
