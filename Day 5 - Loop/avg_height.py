student_heights = [180, 124, 165, 173, 189, 169, 146]

sum = 0
for std_height in student_heights:
  sum += std_height

num_students = 0
for count in student_heights:
  num_students += 1

print(f"total height = {sum}")
print(f"number of students = {num_students}")
print(f"average height = {round(sum /num_students)}")