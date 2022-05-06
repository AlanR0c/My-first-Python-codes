## Yer life in weeks program ##

# This program uses maths and f-Strings and it tells us how many days, weeks, months we have left if we live until 90 years old.

age = input("Please enter yer bloody age, will ya?\n")

age_int = int(age)
days_per_year = 365
weeks_per_year = 52
months_per_year = 12
total_days = 32850
total_weeks = 4680
total_months = 1080
years_left = 90 - age_int
days_left = total_days - days_per_year * age_int
weeks_left = total_weeks - weeks_per_year * age_int
months_left = total_months - months_per_year * age_int

print(f"Ye got {years_left} years, {months_left} months, {weeks_left} weeks and {days_left} days left.")
