import random

passwords = ["phone", "1234", "hack", "script", "lock"]
secret = random.choice(passwords)

print("Guess the password! Choices:", passwords)
for i in range(3):
    guess = input("Try: ")
    if guess == secret:
        print("✅ Access granted!")
        break
else:
    print(f"❌ Access denied. Password was '{secret}'.")