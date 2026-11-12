KURS = {"USD": 16000, "EUR": 17500, "SGD": 12000, "JPY": 110}
jumlah_idr = 5000000
print(f"Rp {jumlah_idr:,} dikonversi ke:")
for kode, kurs in KURS.items():
    asing = jumlah_idr / kurs
    print(f" {kode}: {asing:>10.2f}")