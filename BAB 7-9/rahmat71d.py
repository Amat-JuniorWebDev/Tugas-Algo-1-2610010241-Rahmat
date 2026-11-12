n = 7
print(f"Tabel perkalian {n}:")
print("=" * 18)
for i in range(1, 11):
    print(f" {n} x {i:>2} = {n*i:>3}")
print("=" * 18)
print(f"Total: {sum(n * i for i in range(1, 11))}")