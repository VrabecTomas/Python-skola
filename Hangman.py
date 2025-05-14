import random

word = random.choice(['apple', 'banana', 'grape', 'orange', 'lemon'])
guessed = []
tries = 6

while tries > 0:
    display = ''.join([c if c in guessed else '_' for c in word])
    print(f"Word: {display}  Tries left: {tries}")
    if display == word:
        print("You won!")
        break
    guess = input("Guess a letter: ").lower()
    if guess in word:
        guessed.append(guess)
    else:
        tries -= 1

if tries == 0:
    print(f"You lost! The word was: {word}")