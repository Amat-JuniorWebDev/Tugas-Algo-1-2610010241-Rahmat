kata_uji = ["kasur", "radar", "kodok", "python", "katak", "Anna"]
for kata in kata_uji:
    bersih = kata.lower()
    terbalik = bersih[::-1]
    palindrom = (bersih == terbalik)
    status = "✓ palindrom" if palindrom else "✗ bukan"
    print(f" {kata:<10} → {status}")