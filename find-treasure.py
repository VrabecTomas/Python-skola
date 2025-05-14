import random

spot = random.randint(1, 5)
guess = int(input("Guess the treasure spot (1-5): "))
if guess == spot:
    print("🎉 You found the treasure!")
else:
    print(f"❌ Nope! It was at {spot}.")