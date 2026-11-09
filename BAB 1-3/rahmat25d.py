for tahun in [2020, 2021, 2024, 2100, 2026]:
    if tahun % 4 == 0:
        status = "kabisat"
    else:
        status = "bukan kabisat"
    print(f"Tahun {tahun}: {status}")