<<<<<<< HEAD
# ui.py

def tampilkan_menu():
    print("=" * 30)
    print("        TASKMATE")
    print("=" * 30)
    print("1. Tambah Tugas")
    print("2. Lihat Tugas")
    print("3. Tandai Selesai")
    print("4. Hapus Tugas")
    print("5. Keluar")
    print("=" * 30)


=======
>>>>>>> 259e69b0ad1bbbac2b1b28914d28a0fbfbb00e01
def tampilkan_tugas(tasks):
    print("\n" + "=" * 30)
    print("         DAFTAR TUGAS")
    print("=" * 30)

    if tasks == []:
        print("Belum ada tugas.")
    else:
        nomor = 1
        total = len(tasks)
        selesai = 0

        for task in tasks:
            judul = task["judul"]
            status = task["status"]

            if status.lower() == "selesai":
                selesai += 1

            print(str(nomor) + ". " + judul + " [" + status + "]")
            nomor += 1

        print("-" * 30)
        print("Total tugas  :", total)
        print("Sudah selesai:", selesai)
        print("Belum selesai:", total - selesai)

    print("=" * 30)
    print()