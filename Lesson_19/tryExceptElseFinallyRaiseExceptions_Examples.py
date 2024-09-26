Example-1a: 

def addNumers(num1, num2):
    return (num1 + num2)


print(addNumers(2, 3))
print(addNumers(10, 5))
print(addNumers(2, 'a'))
print(addNumers(99, 1))
print('Execution completed.')

Output:
5
15
TypeError: unsupported operand type(s) for +: 'int' and 'str'

# nothing prints / executes after the error occurred which means the all the code after the error crashes and as a programmer we do not want that on big files.
# to over come this we use try and except.

Example-1b: 

def addNumers(num1, num2):
    try:
        return (num1 + num2)
    except TypeError:
        return ('Invalid input')


print(addNumers(2, 3))
print(addNumers(10, 5))
print(addNumers(2, 'a'))
print(addNumers(99, 1))
print('Execution completed.')

Output: 
5
15
Invalid input
100
Execution completed.
########################################################################################
