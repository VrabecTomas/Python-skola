import random

def dice_roll():
    print("Rolling the dice...")
    roll = random.randint(1, 6)
    print(f"You rolled a {roll}.")

dice_roll()