#task_manager.py
def tambah_tugas(tasks, judul):
    tugas_baru={"judul": judul, "status": "Belum Selesai"}
    tasks.append(tugas_baru)
    print("Tugas berhasil ditambahkan! ")

def hapus_tugas(tasks,index):
    if len(tasks) == 0:
        print("Tidak ada tugas")
        return
    tasks.pop(index)
    print("Tugas berhasil dihapus!")


def tandai_selesai(tasks, index):
    if len(tasks) == 0:
         print("Tidak ada tugas")
    return
        
tasks[index]["status"] = "Selesai"
print("Tugas berhasil ditandai selesai !")


