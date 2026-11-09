tahun_uji = [2020, 2021, 2024, 2100, 2400, 2026, 1900, 2000]
for tahun in tahun_uji:
    if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
        status = "KABISAT"
    else:
        status = "bukan kabisat"
    print(f" {tahun}: {status}")