import random

code = "".join(str(random.randint(1, 6)) for _ in range(4))  
tries = 5  

for _ in range(tries):
    guess = input(f"Zadej svůj 4místný tip (čísla 1-6), zbývá {tries} pokusů: ")
    if guess == code:
        print("Gratulace! Uhodl jsi kód!")
        break
    correct_pos = sum(1 for i in range(4) if guess[i] == code[i])
    correct_num = sum(min(guess.count(d), code.count(d)) for d in set(guess)) - correct_pos
    print(f"Správně: {correct_pos} na místě, {correct_num} špatně umístěné.")
    tries -= 1  
else:
    print(f"Prohrál jsi! Správný kód byl {code}.")