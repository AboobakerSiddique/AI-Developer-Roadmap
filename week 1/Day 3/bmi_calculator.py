#Requirements
#Create a function that takes:
#Weight (kg)
#Height (m)
#Calculate:
#BMI = Weight / (Height × Height)
#Return the BMI.
#Print the result outside the function.

print("-----------BMI Calculator--------------")
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))
print()

def calculate_bmi(weight, height):
    bmi = weight / (height * height)
    return bmi  
print(f"Your BMI is: {calculate_bmi(weight, height):.2f}")
print("your in a healthy range") if 18.5 <= calculate_bmi(weight, height) <= 24.9 else print("your not in a healthy range")