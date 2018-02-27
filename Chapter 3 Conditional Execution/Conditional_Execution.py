"""
IF in Python must be indented

try:
    x= input('Enter an Integer Value \n')
    x= int(x)
    if(x>0):
        print('x is positive')
        print ('This is the if part')
        if(x>9):
            print('x is a 2 digit number')

    elif(x==0):
        print('x is equal to zero')

    else:
        print('This is the else part')

except:
    print('Please enter an Integer')

"""

#Short circuit evaluation of logical expression

#python interpretor intreprets the expression from left to right, so if there are 2 expressions
#to check in a IF and if the first is false then the interpreter will not check the second expression










