def uwu(hari):
    hari_hari = ["senin", "selasa", "rabu", "kamis", "jumat", "sabtu", "minggu"]
    if hari in hari_hari:
        index_hari = hari_hari.index(hari) + 1
        if index_hari >= len(hari_hari):
            index_hari = 0
        return f"Hari ini, Hari {hari.upper()}. Esok hari {hari_hari[index_hari].upper()}"
    else:
        return "Hari-harimu untuk hari esok sudah tidak ada"

while True:
    ask = uwu(input("Masukkan Hari (huruf kecil): "))
    print(ask)
