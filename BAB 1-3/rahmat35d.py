nama = "Rahmat"
ipk = 3.857
saldo = 1500000
print(f"Nama: {nama}")
print(f"IPK 2 desimal     : {ipk:.2f}")
print(f"Padding rata kanan: {ipk:>10.2f}")
print(f"Padding rata kiri : {nama:<15}|")
print(f"Saldo             : Rp {saldo:,}")
print(f"Diskon 25%        : {0.25:.1%}")
print(f"Ekspresi inline   : {2026 - 1}")