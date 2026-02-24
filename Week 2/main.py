# main.py

from ui import tampilkan_menu, tampilkan_tugas
from task_manager import tambah_tugas, hapus_tugas, tandai_selesai
from file_handler import load_data, simpan_data
from validator import validasi_angka, validasi_index


def main():
    # load data awal
    tasks = load_data()

    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu: ")

        # validasi pilihan menu
        pilihan = validasi_angka(pilihan)
        if pilihan is None:
            continue

        if pilihan == 1:
            # tambah tugas
            judul = input("Masukkan judul tugas: ")
            tambah_tugas(tasks, judul)

        elif pilihan == 2:
<<<<<<< HEAD
            tampilkan_tugas(tasks)
            input("Tekan ENTER untuk kembali ke menu...")
=======
            # lihat tugas
            tampilkan_tugas(tasks)
>>>>>>> fe3e6019e9495edab083cbd76a5c0d731847ce8d

        elif pilihan == 3:
            # tandai tugas selesai
            tampilkan_tugas(tasks)
            nomor = input("Pilih nomor tugas: ")
            index = validasi_index(nomor, tasks)
            if index is not None:
                tandai_selesai(tasks, index)

        elif pilihan == 4:
<<<<<<< HEAD
    # hapus tugas
            tampilkan_tugas(tasks)
            nomor = input("Pilih nomor tugas: ")
            index = validasi_index(nomor, tasks)
        if index is not None:
            hapus_tugas(tasks, index)
            input("Tekan ENTER untuk kembali ke menu...")
=======
            # hapus tugas
            tampilkan_tugas(tasks)
            nomor = input("Pilih nomor tugas: ")
            index = validasi_index(nomor, tasks)
            if index is not None:
                hapus_tugas(tasks, index)
>>>>>>> fe3e6019e9495edab083cbd76a5c0d731847ce8d

        elif pilihan == 5:
            # keluar program
            simpan_data(tasks)
            print("Terima kasih sudah menggunakan TaskMate!")
            break

        else:
            print("Pilihan menu tidak valid!")

        # simpan data setiap selesai satu aksi
        simpan_data(tasks)


if __name__ == "__main__":
    main()