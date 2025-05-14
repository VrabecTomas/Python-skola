import random

streak = 0
while True:
    flip = random.choice(["heads", "tails"])
    guess = input("Guess heads or tails: ").lower()
    if guess == flip:
        streak += 1
        print(f"✅ Correct! Streak: {streak}")
    else:
        print(f"❌ Wrong! It was {flip}. Final streak: {streak}")
        break