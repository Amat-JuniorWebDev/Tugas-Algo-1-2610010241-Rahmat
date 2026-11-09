def hitung(a, op, b):
    match op:
        case "+": return a + b
        case "-": return a - b
        case "*": return a * b
        case "/":
            if b == 0: return "Error: bagi nol"
            return a / b
        case _: return f"Operasi '{op}' tidak dikenali"

kasus = [(10, "+", 5), (10, "-", 5), (10, "*", 5),
         (10, "/", 5), (10, "/", 0), (10, "%", 5)]

for a, op, b in kasus:
    hasil = hitung(a, op, b)
    print(f" {a} {op} {b} = {hasil}")