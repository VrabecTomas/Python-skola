def ciferny_soucet(n):
    return sum(int(cifra) for cifra in str(n))

# Příklad použití
cislo = 845444
print(f"Ciferný součet: {ciferny_soucet(cislo)}")
