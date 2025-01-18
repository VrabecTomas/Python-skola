
# Liché nebo sudé číslo
def check_odd_even(number):
    if number % 2 == 0:
        return f"{number} is even."
    else:
        return f"{number} is odd."

# Použití
number = 7
result = check_odd_even(number)
print(result)