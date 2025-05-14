import random, time

nums = [1, 2, 3]
choice = int(input("Pick a number to race (1-3): "))
winner = random.choice(nums)
print("Racing...", end=''); time.sleep(1)
print(f"\n🏁 Number {winner} wins!")
print("✅ You win!" if choice == winner else "❌ You lose.")