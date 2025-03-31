import random

# Generování 10 náhodných čísel
numbers = [random.randint(1, 100) for _ in range(10)]

# Seřazení pole
sorted_numbers = sorted(numbers)

# Výpis výsledků
print("Původní pole:", numbers)
print("Seřazené pole:", sorted_numbers)
