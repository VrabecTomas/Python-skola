import random

u = input("rock, paper, or scissors? ").lower()
c = random.choice(["rock", "paper", "scissors"])
print(f"Computer chose {c}")
if u == c:
    print("Tie!")
elif (u == "rock" and c == "scissors") or (u == "paper" and c == "rock") or (u == "scissors" and c == "paper"):
    print("You win!")
else:
    print("You lose!")
