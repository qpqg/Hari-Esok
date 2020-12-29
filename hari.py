def uwu(hari):
    hari_hari = ["senin", "selasa", "rabu", "kamis", "jumat", "sabtu", "minggu"]
    if hari in hari_hari:
        index_hari = hari_hari.index(hari) + 1
        if index_hari >= 7:
            index_hari = 0
        print(f"Hari ini, Hari {hari.upper()}. Esok hari {hari_hari[index_hari].upper()}")
        # print(f"Hari ini, Hari {hari}. Esok hari {hari_hari[index_hari]}")
    else:
        print("Hari-harimu untuk hari esok sudah tidak ada")
uwu(input("Masukkan Hari (huruf kecil): "))
