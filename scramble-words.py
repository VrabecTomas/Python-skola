import random

words = ['python', 'memory', 'scramble', 'banana', 'keyboard']
word = random.choice(words)
scrambled = ''.join(random.sample(word, len(word)))

print(f"Unscramble: {scrambled}")
guess = input("Your guess: ")

if guess == word:
    print("Correct!")
else:
    print(f"Wrong! It was {word}.")
