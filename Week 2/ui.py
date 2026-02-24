def tampilkan_tugas(tasks):
    print("\nDaftar Tugas:")

    if tasks == []:
        print("Belum ada tugas.")
    else:
        nomor = 1
        for task in tasks:
            print(str(nomor) + ". " + task["judul"] + " [" + task["status"] + "]")
            nomor += 1

    print()