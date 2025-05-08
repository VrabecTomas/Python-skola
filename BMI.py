weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

bmi = weight / (height ** 2)
print(f"\nYour BMI is: {bmi:.1f}")

if bmi < 18.5:
    print("You are underweight.")
elif 18.5 <= bmi < 25:
    print("You are in the normal weight range.")
elif 25 <= bmi < 30:
    print("You are overweight.")
else:
    print("You are obese.")