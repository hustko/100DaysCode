fruits = [4, 55, 64, 32, 16, 32] #find the position of something in a list
x = fruits.index(32)
print(x)

line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = 'B3' # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row

letter = position[0].lower()
rows = ['a','b','c'] 
place = rows.index(letter)

map[int(position[1])-1][place] = 'X'

print(f"{line1}\n{line2}\n{line3}")