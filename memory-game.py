import random
import time
import os

def clear_screen():
    # Works for Windows and Unix/Linux/Mac
    os.system('cls' if os.name == 'nt' else 'clear')

def number_memory_game():
    level = 1
    while True:
        number = ''
        for _ in range(level):
            number += str(random.randint(0, 9))

        print(f"\nLevel {level}")
        print("Remember this number:")
        print(number)
        time.sleep(3)  # Show the number for 3 seconds
        clear_screen()

        guess = input("Enter the number: ")
        if guess == number:
            print("Correct!")
            level += 1
            time.sleep(1)
            clear_screen()
        else:
            print(f"Wrong! The number was {number}.")
            print(f"Your final score: Level {level}")
            break

# Run the game
number_memory_game()
