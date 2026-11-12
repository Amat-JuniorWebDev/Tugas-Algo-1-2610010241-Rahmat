import random
random.seed(42) # untuk hasil konsisten
pilihan = ["batu", "gunting", "kertas"]
print("Simulasi 5 ronde batu-gunting-kertas:")
for ronde in range(1, 6):
    p1 = random.choice(pilihan)
    p2 = random.choice(pilihan)
    if p1 == p2: hasil = "SERI"
    elif (p1 == "batu" and p2 == "gunting") or \
         (p1 == "gunting" and p2 == "kertas") or \
         (p1 == "kertas" and p2 == "batu"):
        hasil = "P1 menang"
    else:
        hasil = "P2 menang"
    print(f" Ronde {ronde}: {p1:<8} vs {p2:<8} → {hasil}")