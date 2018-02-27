"""
print('hello')

print ('this is my first file on the new laptop')

#operators  :  +, - ,   *, /, **; last one is for exponent

print (13/3) #python 2 will truncate the decimal places, python 3 will return float results
print (3**3)

# order of  operations
#  PEDMAS
# Parenthesis
# Exponential
# Multiplication or Division
# Operators with same precedence are as evaluated from left to right

# Modulus and Quotient

quotient = 7//3
print (quotient)

remainder = 7%200
print(remainder)


#Changed my python interpreter from 2.7 to 3.5, that comes pre installed on ubuntu 16.04 lts

# Take user input

inp= input('what is your name? \n')
print(inp)

#take specific type of user input
inp2 = input('enter a integer')
print(int(inp2))



# use mnemonic (memory aid) variable names



month = 9

#Variable names are case sensitive
#print(Month) # Executing this line will give an error.



#Excecises

# 1. Write a program that uses input to prompt a user for their name and then welcomes them.

name = input('Enter your name')
print('hello ', name)




#2.  Exercise 3: Write a program to prompt the user for hours and rate per hour to
# compute gross pay.

hour = input('Enter the number of hours ')
rate = input('Enter the rate per hour ')
gross_pay = float(hour) * float(rate)
print('Pay:',gross_pay)


#Exercise 4: Assume that we execute the following assignment statements:
#width = 17
#height = 12.0
#For each of the following expressions, write the value of the expression and the
#type (of the value of the expression).
#1. width//2
#2. width/2.0
#3. height/3
#4. 1 + 2 * 5



# 1, 8.5, 4.0, 11

width = 17
height = 12.0
#For each of the following expressions, write the value of the expression and the
#type (of the value of the expression).
print (width//2) # gives quotient
print (width/2.0)
print (height/3)
print (1 + 2 * 5)
"""

#Exercise 5: Write a program which prompts the user for a Celsius temperature,
# convert the temperature to Fahrenheit, and print out the converted temperature.




#T(°F) = T(°C) × 9/5 + 32

temp_C = input('Enter the temperature in Degree Celsius')
temp_F  = ((float(temp_C)*9)/5) + 32
print(temp_F)

