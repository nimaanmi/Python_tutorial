Example-1a: 

def addNumbers(num1, num2):
    return (num1 + num2)


print(addNumbers(2, 3))
print(addNumbers(10, 5))
print(addNumbers(2, 'a'))
print(addNumbers(99, 1))
print('Execution completed.')

Output:
5
15
TypeError: unsupported operand type(s) for +: 'int' and 'str'

# nothing prints / executes after the error occurred which means the all the code after the error crashes and as a programmer we do not want that on big files.
# to over come this we use try and except.

Example-1b: 

def addNumbers(num1, num2):
    try:
        return (num1 + num2)
    except TypeError:
        return ('Invalid input')


print(addNumbers(2, 3))
print(addNumbers(10, 5))
print(addNumbers(2, 'a'))
print(addNumbers(99, 1))
print('Execution completed.')

Output: 
5
15
Invalid input
100
Execution completed.
########################################################################################
