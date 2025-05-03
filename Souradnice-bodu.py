# Zadej souřadnice bodu A
x = float(input("Zadej x: "))
y = float(input("Zadej y: "))

# Zkontroluj, jestli bod leží na přímce 3x + 2y - 3 = 0
if 3*x + 2*y - 3 == 0:
    print("Bod A leží na přímce.")
else:
    print("Bod A neleží na přímce.")
