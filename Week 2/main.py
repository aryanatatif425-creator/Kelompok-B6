# main.py (Versi Skeleton / Kerangka Awal)


# import ui
# import task_manager
# import file_handler
# import validator

def main():
    print("--- [SISTEM] Program TaskMate Dimulai ---")
    
    # Dummy file_handler belum siap
    tasks = [
        {"judul": "Tugas PBO", "status": "Belum"},
        {"judul": "Tugas Kalkulus", "status": "Selesai"}
    ]

    #  Buat Main Loop
    while True:
        # Dummy UI (
        print("\n=== MENU UTAMA ===")
        print("1. Tambah Tugas")
        print("2. Lihat Daftar Tugas")
        print("3. Tandai Tugas Selesai")
        print("4. Hapus Tugas")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1-5): ")

        # Kerangka Percabangan (Routing)
        if pilihan == '1':
            print("\n[LOG] Anda masuk ke fitur TAMBAH TUGAS")
            
            
        elif pilihan == '2':
            print("\n[LOG] Anda masuk ke fitur LIHAT TUGAS")
            print(f"[LOG] Data dummy saat ini: {tasks}")
            
            
        elif pilihan == '3':
            print("\n[LOG] Anda masuk ke fitur TANDAI SELESAI")
            
            
        elif pilihan == '4':
            print("\n[LOG] Anda masuk ke fitur HAPUS TUGAS")

            
        elif pilihan == '5':
            print("\n[LOG] Menyimpan data ke file...")
         
            print("[LOG] Keluar dari program. Dadah!")
            break
            
        else:
            print("\n[LOG] Input salah! Pilih 1-5 saja.")

if __name__ == "__main__":
    main()