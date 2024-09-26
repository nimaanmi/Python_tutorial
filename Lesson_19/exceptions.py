Exceptions and Errors

# The try block lets you test a block of code for errors.
# The except block lets you handle the error.
# The else block lets you execute code when there is no error.
# The finally block lets you execute code, regardless of the result of the try- and except blocks.


Example: 
print(x)

Output:
NameError: name 'x' is not defined
########################################################################################
List of all built-in python exceptions: 
https://www.w3schools.com/python/python_ref_exceptions.asp

In Python we raise exceptions	|| In Javascript we can throw errors.
########################################################################################
# How to handle the error/exceptions. we can use the python's try block first.

try:
    print(x)

    # except will catch all errors, so we have to be more specific
except:
    print('There is an error.')

Output: 
There is an error.
########################################################################################
# In placing of following the above steps as 'EXCEPT' will catch all errors.
# we'll not get any useful error. So, we could just catch specific error that might occur.


try:
    print(x)
except NameError:
    print('NameError means that something is probably undefined.')

Output: 
NameError means that something is probably undefined.
########################################################################################
# But it wouldn't catch another error.
# In python, if we try to divide anything with 0, it'll come up with the error: ZeroDivisionError: division by zero


x = 2

try:
    print(x / 0)
except NameError:
    print('NameError means that something is probably undefined.')

Output:
ZeroDivisionError: division by zero
########################################################################################
# How to overcome this

x = 2

try:
    print(x / 0)
except NameError:
    print('NameError means that something is probably undefined.')
except ZeroDivisionError:
    print('Please do not divide by zero.')

Output:
Please do not divide by zero.

# So, we have cut two specific errors and that is still leaving everything else to be caught possibly by an except at the end of this.
# But there are other things we could do as well. It's not always bad to raise an error or let Python raise the error.
########################################################################################
#  Lets say we don't get any error, so we could then try else statement.

x = 2
try:
    print(x/1)
except NameError:
    print('NameError means that something is probably undefined.')
except ZeroDivisionError:
    print('Please do not divide by zero.')
else:
    print('No error!')

Output:
2.0
No error!
########################################################################################
# The Finally block will work no matter if there is an error or not.

x = 2
try:
    print(x/0)
except NameError:
    print('NameError means that something is probably undefined.')
except ZeroDivisionError:
    print('Please do not divide by zero.')
else:
    print('No error.')
finally:
    print('I\'m going to print without or without error.')

Output:
Please do not divide by zero.
I'm going to print with or without error.
########################################################################################
