import math

# Poloměry (v metrech)
r_zeme = 6_371_000
r_slunce = 696_340_000

# Objem a povrch Země
objem_zeme = 4/3 * math.pi * r_zeme**3
povrch_zeme = 4 * math.pi * r_zeme**2

# Objem Slunce
objem_slunce = 4/3 * math.pi * r_slunce**3

# Kolikrát se Země vejde do Slunce (objemově)
pocet_zemi_ve_slunci = objem_slunce / objem_zeme

# Počet Zemí jako korálky po obvodu Slunce
obvod_slunce = 2 * math.pi * r_slunce
pocet_koralek = obvod_slunce / (2 * r_zeme)

# Výstup
print(f"Objem Země: {objem_zeme:.2e} m³")
print(f"Povrch Země: {povrch_zeme:.2e} m²")
print(f"Zemí ve Slunci: {pocet_zemi_ve_slunci:,.0f}")
print(f"Zemí jako korálky kolem Slunce: {pocet_koralek:,.0f}")
