# Average Height #

student_heights = input("Input a list of students' heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
print(student_heights)
count = 0
for heights in student_heights:  
  count += heights  
#Here the For Loop gets all the items from the list and start adding them up and stores the result of the summation. It replicates the sum() function.
count1 = 0
for average_height in student_heights:
  count1 += 1
#Here the For Loop sums the length of the input list and stores the result. In other words, it works exactly in the same way as the len() function :D
final_result = round(count / count1)
#Here we get the result of the summation of the elements of the list and divide it by the length of the list itself, which was stored in the second For Loop, and round the final result up.
print(final_result)


#This is a similar code using the sum() and len() functions

student_heights = input("Input a list of students' heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
print(student_heights)

total_height = sum(student_heights)
