data = input("Enter text to encode: ")
for char in data:
    print("██" if ord(char) % 2 == 0 else "  ", end="")
print("\n(This is just a fake visual.)")
