total = 0
harga = [15000, 8500, 12000, 25000]
print("Belanja:")
for h in harga:
    total += h
    print(f" Tambah Rp {h:>6,} | Total: Rp {total:>7,}")
print("\nDemo augmented:")
x = 10
x += 5; print(f"x += 5 → {x}")
x -= 3; print(f"x -= 3 → {x}")
x *= 2; print(f"x *= 2 → {x}")
x //= 4; print(f"x //= 4 → {x}")