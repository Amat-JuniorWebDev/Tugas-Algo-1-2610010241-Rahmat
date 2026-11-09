nim = "2610010241"
tahun = nim[:4]
prodi = nim[4:7]
urut = nim[7:]
print(f"NIM             : {nim}")
print(f"Tahun masuk     : {tahun}")
print(f"Kode prodi      : {prodi}")
print(f"Nomor urut      : {urut}")
kata = "PYTHON"
print(f"\nDemo slicing '{kata}':")
print(f" [0]     : '{kata[0]}'")
print(f" [-1]    : '{kata[-1]}'")
print(f" [2:5]   : '{kata[2:5]}'")
print(f" [::2]   : '{kata[::2]}'")
print(f" [::-1]  : '{kata[::-1]}'")