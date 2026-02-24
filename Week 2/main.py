# main.py (Versi Skeleton / Kerangka Awal)


# import ui
# import task_manager
# import file_handler
# import validator

def main():
    print("--- [SISTEM] Program TaskMate Dimulai ---")
    
    #  Dummy Data file_handler 
    tasks = [
        {"judul": "Tugas PBO", "status": "Belum"},
        {"judul": "Tugas Kalkulus", "status": "Selesai"}
    ]

    # 3. Buat Main Loop
    while True:
        # Dummy UI 
        print("\n=== MENU UTAMA ===")
        print("1. Tambah Tugas")
        print("2. Lihat Daftar Tugas")
        print("3. Tandai Tugas Selesai")
        print("4. Hapus Tugas")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1-5): ")

        # 4. Buat Kerangka Percabangan (Routing)
        if pilihan == '1':
            print("\n[LOG] Anda masuk ke fitur TAMBAH TUGAS")
            # entar kode di bawah ini akan diaktifkan kalau modulnya sudah siap:
            # judul_baru = input("Masukkan judul: ")
            # if validator.cek_input_kosong(judul_baru):
            #     tasks = task_manager.tambah_tugas(tasks, judul_baru)
            
        elif pilihan == '2':
            print("\n[LOG] Anda masuk ke fitur LIHAT TUGAS")
            print(f"[LOG] Data dummy saat ini: {tasks}")
            # entar diganti dengan: ui.tampilkan_daftar_tugas(tasks)
            
        elif pilihan == '3':
            print("\n[LOG] Anda masuk ke fitur TANDAI SELESAI")
            # entar diisi logika memanggil task_manager.tandai_selesai()
            
        elif pilihan == '4':
            print("\n[LOG] Anda masuk ke fitur HAPUS TUGAS")
            # entar diisi logika memanggil task_manager.hapus_tugas()
            
        elif pilihan == '5':
            print("\n[LOG] Menyimpan data ke file...")
            # entar diganti dengan: file_handler.simpan_data("data.txt", tasks)
            print("[LOG] Keluar dari program. Dadah!")
            break
            
        else:
            print("\n[LOG] Input salah! Pilih 1-5 saja.")

if __name__ == "__main__":
    main()