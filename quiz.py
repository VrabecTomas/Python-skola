questions = {
    "What is the capital of France? ": "paris",
    "2 + 2 = ": "4",
    "What color is the sky? ": "blue"
}

score = 0
for q, a in questions.items():
    if input(q).lower() == a:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The answer was {a}.")

print(f"Your score: {score}/{len(questions)}")