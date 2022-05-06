#BMI Calculator 2.0#

# This program calculates the Body Mass Index(BMI)from a user's weight and height. This program returns the exact results to the user.

height = float(input("Please enter your height in m: "))
weight = float(input("Please enter your weight in kg: "))


bmi = weight / height ** 2 #-> height to the power of 2

if bmi < 18.5:
  print(f"Your BMI is {round(bmi)}, you are underweight.")
elif bmi < 25:
  print(f"Your BMI is {round(bmi)}, you have a normal weight.")
elif bmi < 30:
  print(f"Your BMI is {round(bmi)}, you are slightly overweight.")
elif bmi < 35:
  print(f"Your BMI is {round(bmi)}, you are obese.")
else:
  print(f"Your BMI is {round(bmi)}, you are clinically obese.")
