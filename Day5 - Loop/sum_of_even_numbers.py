target = 100
total = 0
#start from 2 anyways cus that is the first even number
#stop = is target +1 or else it wont be counted
# step = 2 instead of finding modulus so that it increments by 2 steps 
for number in range(2,target+1,2):
  total +=number

print(total)