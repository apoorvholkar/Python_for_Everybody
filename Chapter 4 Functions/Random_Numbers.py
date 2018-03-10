"""
Given the same input "Deterministic values" will return the same output values each time the program
is run

Pseudo-random numbers are not truly random numbers as they are generated from deterministic operations

"""
import random

"""
for i in range(10):
    #x=random.random()
    x=random.randint(5,10)
    print(i,x)
"""

t=[1,2,3,4,5,10]
t1= random.choice(t)
print(t1)
