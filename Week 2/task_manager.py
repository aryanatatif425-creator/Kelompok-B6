def tambah_tugas(tasks):
    judul = input("Masukkan judul tugas: ")

    tugas_baru = {
        "judul": judul,
        "status": "Belum Selesai"
    }

    tasks.append(tugas_baru)
    print("Tugas berhasil ditambahkan!")

    def hapus_tugas(tasks):
        if len(tasks) == 0:
            print("Tidak ada tugas")
            return 
        index = int(input("Masukkan nomor tugas yang ingin anda hapus: : "))
        if 0 <= index < len(tasks):
            tasks.pop(index)
            print("Tugas berhasil dihapus! ")
        else:
            print("Nomor tugas tidak valid !")


    def tanai_selesai(tasks):
        if len(tasks) == 0:
            print("Tidak ada tugas")
            return
        
        index = int(input("Masukkan nomer tugas yang ingin anda tandai selesai: "))

        if 0 <= index < len(tasks):
            tasks[index]["status"] = "Selesai"
            print("Tugas berhasil ditandai selesai! ")
        else:
            print("Nomor tugas tidak valid !")

        def lihat_tugas(tasks):
            if len(tasks) == 0:
                print("Tidak ada tugas")
            return
        
        print("\nDaftar Tugas: ")
        for i in range(len(tasks)):
            print(i, "-", tasks[i]["judul"] + " [" , tasks[i]["status"] + "]")

