# import random

# for i in range(5):
#     value = random.randint(1, 6)
#     print(value)

# import random
# random.seed(int(input())) #please don't touch this lane

# #generate the random values for every dice
# dice1 = random.randint(1,6)
# dice2 = random.randint(1,6)

# print(dice1)
# print(dice2)   

# from math import pi
# print(pi)

# from math import sqrt as square_root
# print(square_root(100))

# import math as m
# print(math.sqrt(25))

# def print_nums(x):
#   for i in range(x):
#     print(i)
#     return
# print_nums(10)

def func(x):
  res = 0
  for i in range(x):
     res += i
  return res

print(func(4))
