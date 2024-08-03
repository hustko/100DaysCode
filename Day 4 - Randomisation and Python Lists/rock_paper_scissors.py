import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

person = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissor.\n"))
computer_choice = random.randint(0,1)

if person == 0:
    print(rock)
elif person == 1:
    print(paper)
else:
    print(scissors)

print("Computer chose\n")
if computer_choice == 0:
    print(rock)

elif computer_choice == 1:
    print(paper)
else:
    print(scissors)

if person >= 3 or person < 0:
    print("Invalid number")
elif person == 0 and computer_choice == 2 :
    print("You win")
elif person == 2 and computer_choice == 0 :
    print("You lose")
elif computer_choice < person:
    print("You win")
elif computer_choice > person:
    print("You lose")
elif computer_choice == person:
    print("Draw!")






