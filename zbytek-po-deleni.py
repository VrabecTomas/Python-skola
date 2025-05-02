def custom_modulo(a, b):
    if b == 0:
        return None  # dělení nulou není povoleno
    q = a // b      # celé dělení
    r = a - q * b   # výpočet zbytku
    return r

# Test
a = 7400
b = 400
print(f"Zbytek po dělení {a} / {b} je {custom_modulo(a, b)}")