while True:
    try:
        weight = float(input("Enter your weight (in kg): "))
        if weight <= 0:
            print("Weight must be greater than 0!")
            continue
        height = float(input("Enter your height (in m): "))
        if height <= 0 or height > 2.5:
            print("Height must be between 0 and 2.5 m!")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a number.")

bmi = weight / height ** 2
print(f"Your BMI is: {bmi:.2f}")

if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal weight"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obesity"

print(f"BMI Category: {category}")