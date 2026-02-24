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