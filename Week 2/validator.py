# validator.py

def validasi_angka(input_user):
    """
    Mengubah input menjadi integer jika memungkinkan.
    Return integer jika valid.
    Return None jika tidak valid.
    """
    try:
        angka = int(input_user)
        return angka
    except ValueError:
        print("Input harus berupa angka!")
        return None


def validasi_index(input_user, tasks):
    """
    Memvalidasi apakah index yang dimasukkan user valid.
    Return index (int) jika valid.
    Return None jika tidak valid.
    """
    angka = validasi_angka(input_user)

    if angka is None:
        return None

    # Karena user lihat nomor mulai dari 1,
    # sedangkan index list mulai dari 0
    index = angka - 1

    if 0 <= index < len(tasks):
        return index
    else:
        print("Nomor tugas tidak valid!")
        return None