nilai_list = [92, 85, 78, 70, 65, 50, 30]
for nilai in nilai_list:
    if nilai >= 85: huruf = "A"
    elif nilai >= 75: huruf = "B"
    elif nilai >= 65: huruf = "C"
    elif nilai >= 55: huruf = "D"
    else: huruf = "E"
    lulus = "LULUS" if nilai >= 60 else "TIDAK LULUS"
    print(f" Nilai {nilai:>3} → Huruf {huruf} ({lulus})")