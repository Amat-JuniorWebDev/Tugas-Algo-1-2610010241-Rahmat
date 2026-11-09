data = [(65, 170), (50, 165), (85, 168), (110, 175)]
for berat, tinggi_cm in data:
    tinggi_m = tinggi_cm / 100
    imt = berat / (tinggi_m ** 2)
    if imt < 18.5: kategori = "Kurus"
    elif imt < 25: kategori = "Normal"
    elif imt < 30: kategori = "Kelebihan berat"
    else: kategori = "Obesitas"
    print(f"BB {berat:>3}kg, TB {tinggi_cm}cm → IMT {imt:>5.2f} ({kategori})")