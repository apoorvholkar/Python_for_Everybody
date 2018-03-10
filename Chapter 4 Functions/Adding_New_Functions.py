#defining a function without any arguments
def hello():
    print('Hello this is my first function')

#calling a function that does not take any arugments.
#hello()

# defining a function with arguments
def sum1(x,y):
    print(x+y)

#sum1(10.1,5)

# you can call a function inside another function
# the below function will call the two functions that are defined above

def fuct_in_func(x,y):
    hello()
    sum1(x,y)


fuct_in_func(11,12.2)

#even if i define Sum1 after func_in_func as long as func_in_func is not called yet, the program will exectue just fine.







