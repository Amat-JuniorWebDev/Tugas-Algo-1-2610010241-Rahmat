nilai = [10, 3.14, "halo", True, None, [1,2], (3,4), {1,2}, {"a":1}]
for v in nilai:
    print(f"{str(v):<15} → {type(v).__name__}")