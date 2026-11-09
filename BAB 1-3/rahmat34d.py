print("Tipe dari 5 :", type(5))
print("Tipe dari 5.0:", type(5.0))
print("Tipe dari 'a':", type('a'))
halo = print
halo("Saya bisa dipanggil dengan nama baru!")
print()
print("Nama fungsi:", print.__name__)
kotak = [10, "halo", 3.14, print]
kotak[3]("Memanggil print dari list!")