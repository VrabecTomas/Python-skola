import random

score = 0

for i in range(5):
    a, b = random.randint(1, 10), random.randint(1, 10)
    op = random.choice(['+', '-', '*'])
    answer = eval(f'{a}{op}{b}')
    user = int(input(f'{a} {op} {b} = '))
    if user == answer:
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong. The answer was {answer}.\n")

print(f'Your score: {score}/5')