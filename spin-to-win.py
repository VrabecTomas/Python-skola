import random

lucky = int(input("Pick your lucky number (1-10): "))
spin = random.randint(1, 10)
print(f"🎲 Spinning... It's {spin}!")
print("🎉 You win!" if lucky == spin else "😢 Better luck next time.")