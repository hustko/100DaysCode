import random #import random module
#random is like a car, one person cannot build the whole car, so each part is assigned to a person like tire module, engine module etc
#when a system is built and the code is large and long it is split into module
#below the module.py is imported
import my_module

print(my_module.pi)

num = random.randint(1,10) #randint gives num between 1 and 10 inclusive
print(num)
float_num = random.random() #get a random floating point betwen 0.0 to 1.0
print(float_num)

#create random float between 0 to 5
more_float = random.random()*5
print(more_float)