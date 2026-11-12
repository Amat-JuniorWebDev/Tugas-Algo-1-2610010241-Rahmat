def is_prima(n):
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0: return False
    return True
for n in [7, 12, 17, 25, 29, 31, 100, 97]:
    status = "PRIMA" if is_prima(n) else "bukan prima"
    print(f" {n:>4}: {status}")