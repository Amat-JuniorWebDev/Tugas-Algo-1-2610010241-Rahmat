bilangan = [3, 8, 11, 20, 27]
for n in bilangan:
    if n % 2 == 0:
        keterangan = "genap"
    else:
        keterangan = "ganjil"
    print(f"{n:>3} adalah {keterangan}")