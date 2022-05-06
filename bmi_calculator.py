# BMI Calculator #

# This program calculates the Body Mass Index(BMI) from a user's weight and height.


height = input('Please enter yer height in metres, as shown in the following example -> "1.70":\n')
weight = input('Please enter yer weight in kg, as shown in the following example -> "70":\n')

result1 = float(height)
result2 = int(weight)
final_result = result2 / result1 ** 2
print(int(final_result))
