kata = "Python"
metode = [m for m in dir(kata) if not m.startswith("_")]
print(f"Jumlah metode string: {len(metode)}")
print("10 metode pertama:")
for m in metode[:10]:
    print(f" - {m}")