def hitung_bmi(berat, tinggi_cm):
    tinggi_m = tinggi_cm / 100
    bmi = berat / (tinggi_m ** 2)
    if bmi < 18.5: kat = "Kurus"
    elif bmi < 25: kat = "Normal"
    elif bmi < 30: kat = "Berlebih"
    else: kat = "Obesitas"
    return bmi, kat

orang = [("Andi", 65, 170), ("Budi", 80, 168), ("Cici", 50, 160)]
for nama, b, t in orang:
    bmi, kat = hitung_bmi(b, t)
    print(f" {nama:<6}: BB {b}kg TB {t}cm → BMI {bmi:.2f} ({kat})")