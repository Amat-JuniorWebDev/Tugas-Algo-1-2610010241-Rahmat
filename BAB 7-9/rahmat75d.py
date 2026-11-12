n = 10
print("Memulai hitung mundur:")
while n > 0:
    print(f"  T-minus {n}...")
    n -= 1
print("✨ LEPAS LANDAS! ✨")

print("\nMencari kelipatan 7 pertama yang > 50:")
n = 1
while True:
    if n * 7 > 50:
        print(f"  Ditemukan: {n} x 7 = {n * 7}")
        break
    n += 1