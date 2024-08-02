# Input a list of student scores
student_scores = [78, 65, 89, 86, 55, 91, 64, 89]

# Write your code below this row 👇
max = 0
for score in student_scores:
  if score >= max:
    max = score

print(f"The highest score in the class is: {max}")