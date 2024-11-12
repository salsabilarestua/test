def penambahan(jadwal):
    
    hari = input("Masukkan hari (Senin, Selasa, dst): ")
    waktu = input("Masukkan waktu (misal: 08:00 - 10:00): ")
    matkul = input("Masukkan nama mata kuliah: ")
    
    if hari not in jadwal:
        jadwal[hari] = []
    
    jadwal[hari].append({'waktu': waktu, 'mata_kuliah': matkul})
    print("Jadwal berhasil ditambahkan!\n")

# Fungsi untuk menampilkan seluruh jadwal kuliah
def tampilan(jadwal):
    if not jadwal:
        print("Jadwal kuliah kosong.\n")
        return

    for hari, jadwal_hari in jadwal.items():
        print(f"Jadwal untuk hari {hari}:")
        for item in jadwal_hari:
            print(f"  Waktu: {item['waktu']} - Mata Kuliah: {item['mata_kuliah']}")
        print()  # baris kosong setelah jadwal per hari

def main():
    jadwal = {}  
    
    while True:
        print("1. Tambah Jadwal Kuliah")
        print("2. Tampilkan Jadwal Kuliah")
        print("3. Keluar")
        
        pilihan = input("Pilih menu (1/2/3): ")
        
        if pilihan == "1":
            penambahan(jadwal)
        elif pilihan == "2":
            tampilan(jadwal)
        elif pilihan == "3":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih 1, 2, atau 3.")

if __name__ == "__main__":
    main()
