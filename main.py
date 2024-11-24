import time
from utils import helper
from function import (
    jadwalkuliah,
    login,
    timerBelajar,
    tipsBelajar
)

def interface(username):
    # Interface utama yang memuat semua fitur setelah user melakukan login
    while True:
        helper.clear()
        print(f"Selamat datang {username} di aplikasi Helper Mahasiswa!\n")
        print("1. Timer Belajar")
        print("2. Atur Jadwal Kuliah")
        print("3. Exit")
        choice = input("Pilih dengan angka: ")

        if choice == '1':
            helper.clear()
            timerBelajar.timerSetup()
        elif choice == '2':
            helper.clear()
            jadwalkuliah.main()
        elif choice == '3':
            print("\nTerima kasih telah menggunakan aplikasi Helper Mahasiswa!")
            break
        else:
            print("\nInvalid input! Silakan coba lagi.")
            time.sleep(1)

def main():
    username = login.main()
    if username == "admin":
        tipsBelajar.main(username)
    elif username:
        interface(username)
    

if __name__ == "__main__":
    main()