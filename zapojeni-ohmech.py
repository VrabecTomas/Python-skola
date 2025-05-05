def vypocet_odporu(R1, R2):
    serie = R1 + R2
    paralelne = (R1 * R2) / (R1 + R2)
    return serie, paralelne

# Příklad použití
R1 = 100  # Ohm
R2 = 200  # Ohm
s, p = vypocet_odporu(R1, R2)
print(f"Sériově: {s} Ω, Paralelně: {p:.2f} Ω")
