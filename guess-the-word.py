import random
words = ["apple", "banana", "cherry"]
word = random.choice(words)
while True:
    guess = input("Guess the word: ")
    if guess == word:
        print("You guessed it!")
        break
    else:
        print("Try again!")
