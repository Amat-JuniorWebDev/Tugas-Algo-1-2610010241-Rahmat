hari_list = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat",
             "Sabtu", "Minggu"]
hari_kerja = {"Senin", "Selasa", "Rabu", "Kamis", "Jumat"}

for hari in hari_list:
    if hari in hari_kerja: kategori = "Hari kerja"
    else: kategori = "Akhir pekan"
    
    if hari == "Jumat": suasana = "— hampir akhir pekan!"
    elif hari == "Senin": suasana = "— awal minggu"
    elif hari in ("Sabtu", "Minggu"): suasana = "— saatnya santai"
    else: suasana = ""
    
    print(f" {hari:<8}: {kategori} {suasana}")