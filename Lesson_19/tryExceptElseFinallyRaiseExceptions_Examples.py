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
Example-2a:

def addNumbers(num1, num2):
    try:
        return (num1 + num222)
    except TypeError:
        return ('Invalid input')


print(addNumbers(2, 3))
print(addNumbers(10, 5))
print(addNumbers(2, 'a'))
print(addNumbers(99, 1))
print('Execution completed.')

Output:
NameError: name 'num222' is not defined. Did you mean: 'num2'?

# In the return we entered incorrect parameters.
# Here we are seeing a second type of error and nothing gets executed, which means the whole block of code crashes.
# To overcomes this, we could raise a second exception.

Example-2b:

def addNumbers(num1, num2):
    try:
        return (num1 + num2)
    except TypeError:
        return ('Invalid input')
    except NameError:
        return ('NameError means that something is probably undefined.')


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

# Even here, it excecutes all the codes and just raises error where we used ty and except, saving the entire code from crashing.
########################################################################################
Example-3a:

def addNumbers(num1, num2):
    try:
        return (num1 + num2)
    # except TypeError:
    #     return ('Invalid input')
    # except NameError:
    #     return ('NameError means that something is probably undefined.')
    except Exception as error:
        return (error)


print(addNumbers(2, 3))
print(addNumbers(10, 5))
print(addNumbers(2, 'a'))
print(addNumbers(99, 1))
print('Execution completed.')

Output: 
5
15
unsupported operand type(s) for +: 'int' and 'str'
100
Execution completed.

# except Exception is standard exception type which will satisfy ANY type of exception that can occur.
# all these are inbuilt exception types.
# except Exception is always used at the end of the try and except, if we used it in the starting it'll ignore any except below it.
########################################################################################

