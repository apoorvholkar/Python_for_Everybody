"""
Exercise 1: Rewrite your pay computation to give the employee 1.5 times the
hourly rate for hours worked above 40 hours.
Enter Hours: 45
Enter Rate: 10
Pay: 475.0


hour = input('Enter the number of hours ')
rate = input('Enter the rate per hour ')
if(float(hour)>40):
    gross_pay = (1.5 * (float(hour)-40) * float(rate)) + (40 * float(rate))
    print('Pay:',gross_pay)
else:
    gross_pay = float(hour) * float(rate)
    print('Pay:',gross_pay)


Exercise 2: Rewrite your pay program using try and except so that your pro-
gram handles non-numeric input gracefully by printing a message and exiting the
program. The following shows two executions of the program:
Enter Hours: 20
Enter Rate: nine
Error, please enter numeric input
Enter Hours: forty
Error, please enter numeric input

try:
    hour = input('Enter the number of hours ')
    hour = float(hour)
    rate = input('Enter the rate per hour ')
    rate = float(rate)
    gross_pay = float(hour) * float(rate)
    print('Pay:',gross_pay)
except:
    print('Error, please enter numeric input')

Exercise 3: Write a program to prompt for a score between 0.0 and 1.0. If the
score is out of range, print an error message. If the score is between 0.0 and 1.0,
print a grade using the following table:
Score   Grade
>= 0.9  A
>= 0.8  B
>= 0.7  C
>= 0.6  D
< 0.6   F

Enter score: 0.95
A
Enter score: perfect
Bad score
Enter score: 10.0
Bad score
Enter score: 0.75
C
Enter score: 0.5
F
Run the program repeatedly as shown above to test the various different values for
input.


"""
try:
    score = input('Enter your score between 0.0 and 1.0 \n')
    score = float(score)
    if (score>= 0.9 and score <=1.0):
        print('Grade: A')
    elif(score>= 0.8 and score <0.9):
        print('Grade: B')
    elif(score>= 0.7 and score <0.8):
        print('Grade: C')
    elif(score >= 0.6 and score < 0.7):
        print('Grade: D')
    elif(score <0.6):
        print('Grade: E')
    else:
        print('Error, score is out of range')

except:
    print('Error, please enter numeric values')