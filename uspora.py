vklad = float(input("Zadej počáteční vklad (Kč): "))
urok = float(input("Zadej roční úrokovou míru (%): "))
roky = int(input("Zadej dobu úspor (v letech): "))

# Výpočet úroku (jednoduché úročení)
vzrust = vklad * (urok / 100) * roky
konecna_castka = vklad + vzrust

print(f"Vaše úspora vzroste o {vzrust:.2f} Kč.")
print(f"Celková částka po {roky} letech bude {konecna_castka:.2f} Kč.")
