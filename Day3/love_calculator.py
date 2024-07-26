print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
names = name1.lower() + name2.lower()

t = names.count("t")
r = names.count("r")
u = names.count("u")
e = names.count("e")

l = names.count("l")
o = names.count("o")
v = names.count("v") 
e = names.count("e") 

true = t + r + u + e
love = l + o + v + e

total = str(true) + str(love)

if int(total) < 10 or int(total) > 90:
  print(f"Your score is {total}, you go together like coke and mentos.")
elif 40<int(total)<50:
  print(f"Your score is {total}, you are alright together.")
else:
  print(f"Your score is {total}.")