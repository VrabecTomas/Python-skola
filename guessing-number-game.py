import random

secret_number = random.randint(1, 10)
guess = int(input("Guess a number between 1 and 10: "))
print("Correct!" if guess == secret_number else "Wrong!")