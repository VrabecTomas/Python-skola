import random as r
b = [" "] * 9; w = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
for _ in range(9):
    print(f"{b[0]}|{b[1]}|{b[2]}\n-+-+-\n{b[3]}|{b[4]}|{b[5]}\n-+-+-\n{b[6]}|{b[7]}|{b[8]}")
    if b.count(" ") % 2 == 0:
        c = r.choice([i for i, v in enumerate(b) if v == " "]); b[c] = "O"
        if any(b[i]==b[j]==b[k]=="O" for i,j,k in w): print("Computer wins!"); break
    else:
        m = int(input("Your move (0-8): "))
        if b[m] != " ": continue
        b[m] = "X"
        if any(b[i]==b[j]==b[k]=="X" for i,j,k in w): print("You win!"); break
else: print("Tie!")
