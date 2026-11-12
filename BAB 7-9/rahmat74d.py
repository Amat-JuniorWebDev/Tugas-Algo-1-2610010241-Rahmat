n = 6
print("Pola 1: Segitiga siku-kiri")
for i in range(1, n + 1):
    print("*" * i)
print()
print("Pola 2: Segitiga sama kaki")
for i in range(1, n + 1):
    spasi = " " * (n - i)
    bintang = "*" * (2 * i - 1)
    print(spasi + bintang)
print()
print("Pola 3: Segitiga terbalik")
for i in range(n, 0, -1):
    print("*" * i)