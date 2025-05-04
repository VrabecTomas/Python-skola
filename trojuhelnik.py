# Načtení délek stran
a = float(input("Zadej délku strany a: "))
b = float(input("Zadej délku strany b: "))
c = float(input("Zadej délku strany c: "))

# Ověření trojúhelníkové nerovnosti
if a + b > c and a + c > b and b + c > a:
    print("Lze sestavit trojúhelník.")
else:
    print("Nelze sestavit trojúhelník.")
