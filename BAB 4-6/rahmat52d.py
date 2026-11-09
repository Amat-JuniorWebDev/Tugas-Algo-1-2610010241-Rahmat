pi = 3.141592653589793
harga = 1250000
diskon = 0.15
print(f"Pi default      : {pi}")
print(f"Pi 2 desimal    : {pi:.2f}")
print(f"Pi 4 desimal    : {pi:.4f}")
print(f"Harga           : Rp {harga:,}")
print(f"Diskon          : {diskon:.0%}")
print(f"Setelah diskon  : Rp {harga * (1 - diskon):,.0f}")
print()
print(f"{'Item':<10}{'Harga':>10}")
print("-" * 20)
print(f"{'Buku':<10}{50000:>10,}")
print(f"{'Pulpen':<10}{12500:>10,}")