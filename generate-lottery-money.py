import random

def generate_lottery_number():
  # Generate a random 6-digit lottery number
  lottery_number = ""
  for i in range(6):
    lottery_number += str(random.randint(0, 9))
  return lottery_number

print(generate_lottery_number())