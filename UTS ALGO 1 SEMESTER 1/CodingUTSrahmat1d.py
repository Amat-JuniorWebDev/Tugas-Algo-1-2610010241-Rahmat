# Deklarasi Variabel
nama = "Rina"
nilai_1 = 85
nilai_2 = 78
nilai_3 = 92


# Perhitungan
total = nilai_1 + nilai_2 + nilai_3
rata_rata = total/3
persentase = (total / 300) * 100
lulus = rata_rata >= 75

# Menampilkan Output Sesuai Format
print("====================================")
print("        KARTU NILAI SEMENTARA")
print("====================================")
print(f"Nama         : {nama}")
print(f"Nilai 1      : {nilai_1}")
print(f"Nilai 2      : {nilai_2}")
print(f"Nilai 3      : {nilai_3}")
print("------------------------------------")
print(f"Total        : {total}")
print(f"Rata-Rata    : {rata_rata:.2f}")
print(f"Presentase   : {persentase:.1f}%")
print(f"Lulus        : {lulus}")
print('====================================')