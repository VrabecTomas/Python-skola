
# Enter a number in the decimal system
decimal_number = int(input("Enter a number in decimal: "))

# Convert to binary system
binary_number = bin(decimal_number)

# Display the result (without the '0b' prefix)
print("The number in binary is:", binary_number[2:])
