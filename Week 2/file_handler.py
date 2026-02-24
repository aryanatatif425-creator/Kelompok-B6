# file_handler.py
# testing commit
"""Simple file handler untuk TaskMate.

Format file yang digunakan: judul|status
Contoh baris: Tugas PBO|Belum

Fungsi yang disediakan:
- load_data() -> list of tasks (dict: {'judul','status'})
- simpan_data(tasks) -> menulis list tasks ke file (tidak mengembalikan apa-apa)

File default: data.txt
"""

DATA_FILE = "data.txt"


def load_data():
    """Membaca file DATA_FILE dan mengembalikan list tugas.

    Returns:
        list: setiap elemen adalah dict dengan kunci 'judul' dan 'status'.
    """
    tasks = []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                # Pisah hanya pada pemisah pertama sehingga judul boleh mengandung '|'
                parts = line.split("|", 1)
                if len(parts) == 2:
                    judul = parts[0].strip()
                    status = parts[1].strip()
                else:
                    # Jika format tidak sesuai, anggap seluruh baris sebagai judul
                    judul = parts[0].strip()
                    status = "Belum"
                tasks.append({"judul": judul, "status": status})
    except FileNotFoundError:
        # Jika file belum ada, kembalikan list kosong
        return []
    return tasks


def simpan_data(tasks):
    """Menyimpan list tugas ke DATA_FILE.

    Args:
        tasks (list): list dict dengan kunci 'judul' dan 'status'.

    Fungsi ini tidak mengembalikan apa-apa.
    """
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        for t in tasks:
            judul = str(t.get("judul", "")).replace("\n", " ").replace("|", " ")
            status = str(t.get("status", "Belum")).replace("\n", " ").replace("|", " ")
            f.write(f"{judul}|{status}\n")
