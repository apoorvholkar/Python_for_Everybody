#Updating Variables:

"""
x= 1;
x = x+1;
print(x)

# WHILE Statement

n= 5;
while n>0:
    print(n)
    n = n-1;
print("Blastoff")

# Infinite loops and break

while True:
    line = input(' >  ')
    if line =='done':
        break
    print(line)
print("Done!")


"""

# Finishing iterations with "continue"

# continue will skip the execution of the current loop and jump to the next iteration or statement

while True:
    line = input('>-')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print("Done!")


