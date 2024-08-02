#Password Generator Project
#Day 5
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to PyPassword Generator!")
num_of_letters = int(input("How many letters would you like in your password?\n"))
num_of_symbols = int(input("How many symbols would you like?\n"))
num_of_numbers = int(input("How many numbers would you like?\n"))

#testing inputs are below; then comment above
# num_of_letters = 4
# num_of_symbols = 2
# num_of_numbers = 2

#Eazy Level - Order not randomised it is sequential:
easy_password = '' 
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

for letter in range(num_of_letters):
    easy_password += random.choice(letters)

for symbol in range(num_of_symbols):
    easy_password += random.choice(symbols)

for symbol in range(num_of_numbers):
    easy_password += random.choice(numbers)

print(f"Here is your easy level password: {easy_password}")

#Hard Level - Order of characters randomised, hence shuffled:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
hard_password = list(easy_password)
random.shuffle(hard_password)

pwd = ''
for char in hard_password:
    pwd += char
    
print(f"Here is your hard level password: {pwd}")