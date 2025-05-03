for i in range(8):
    row = ""
    for j in range(8):
        if (i + j) % 2 == 0:
            row += "0"
        else:
            row += "1"
    print(row)
