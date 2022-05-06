# Highest Score #

student_scores = input("Please enter a list of students scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

biggest_number = 0
for number in student_scores:
  if biggest_number < 0 or biggest_number < number: #I could have also just coded -> if number > biggest_number
    biggest_number = number
print(f"The highest score is {biggest_number}.")


#This is another version of the code above.

#After analysing the code, I've realised I could remove the first condition of the if statement(biggest_number is None). Also, I had to change the counter value, that is, instead of coding "None", I coded "0". The reason for this change, None to 0, is because if I hadn't changed it, the program would be buggy and this error message would pop up in the console: if (number > biggest_number):
# TypeError: '>' not supported between instances of 'int' and 'NoneType'

student_scores = input("Please enter a list of students scores\n").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

biggest_number = 0
for number in student_scores:
  if number > student_scores:
    biggest_number = number
print(biggest_number)
