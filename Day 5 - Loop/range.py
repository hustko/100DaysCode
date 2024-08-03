#the range takes nums from 1 to 10 without 10
#thus 1 to 9
for num in range(1,10):
    print(num)

#to get list from 1 to 10
#as u can see in output, the step count increases by 1
for num in range(1, 11):
    print(num)

#to increase step
for num in range(1,11,2):
    print(num)
#output is 1, 3, 5, 7, 9 no 11 cus the stop is omitted


#find the sum for every number from 1 to 100
total = 0
for num in range(1,101):
    total+=num
print(total)
