import random

size = 5
mines_count = 5
mines = set()
revealed = set()

# Generuj miny
while len(mines) < mines_count:
    mines.add((random.randint(0, 4), random.randint(0, 4)))

# Pomocná funkce
def parse(coord):
    if len(coord) != 2: return None
    row = ord(coord[0].upper()) - ord('A')
    col = int(coord[1]) - 1
    if 0 <= row < size and 0 <= col < size:
        return (row, col)
    return None

def neighbors(r, c):
    return [(r+i, c+j) for i in (-1,0,1) for j in (-1,0,1)
            if 0 <= r+i < size and 0 <= c+j < size and (i, j) != (0, 0)]

def count_adjacent_mines(r, c):
    return sum((nr, nc) in mines for nr, nc in neighbors(r, c))

def print_board():
    print("  1 2 3 4 5")
    for i in range(size):
        row = chr(ord('A')+i) + ' '
        for j in range(size):
            if (i, j) in revealed:
                if (i, j) in mines:
                    row += 'X '
                else:
                    row += str(count_adjacent_mines(i, j)) + ' '
            else:
                row += '. '
        print(row)

# Hlavní smyčka
print("💣 Hra Miny – najdi bezpečná pole!")
while True:
    print_board()
    move = input("Zadej souřadnici (např. A1): ")
    cell = parse(move)
    if not cell or cell in revealed:
        print("Neplatný tah.")
        continue
    revealed.add(cell)
    if cell in mines:
        print_board()
        print("💥 Bum! Prohrál jsi.")
        break
    if len(revealed - mines) == size*size - mines_count:
        print_board()
        print("🎉 Vyhrál jsi! Všechny miny jsi obešel.")
        break
