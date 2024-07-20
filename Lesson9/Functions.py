Functions:
Functions are reusable blocks of code, and when we call a funciton it runs the block of code inside the function.

define a function
name the function
enter the block of code to perform inside the function
call the function.

def hello():					# we define the function by 'def' and we name the function by hello(),, make sure to use the paranthesis/round brackets.
    print('Hello world!')


hello()						# we are calling that function, make sure to use the name of the function and the paranthesis/round brackets.

Output:
Hello world!
########################################################################################

How to name a function
1. hello()					# all lowered letters
2. hello_world()				# separating two words with underscor

Sometimes functions need to receive data and we can use placeholders for that data. Those placeholders are called parameters.
When we call the function and we pass in the actual data, we are passing in arguments.

def sum(num1, num2):
    print(num1 + num2)


sum(2, 3)

Output:
5
########################################################################################

A distinction between parameters and arguments that we pass in, is that parameters never change however arguments can change with every function call.
All of the function calls are reusing the code that we defined for our function sum.

def sum(num1, num2):
    print(num1 + num2)


sum(2, 3)
sum(8, 4)
sum(3, 1000)

Output:
5
12
1003
########################################################################################

Our function isn't really too useful if it just prints this value to the console, we might want to return that value and use in our program
So in place of print, we use return which returns the value - the total of the two parameters.

def sum(num1, num2):
    return num1 + num2


total = sum(1, 3)
print(total)

Output:
4
########################################################################################

Right now our sum function is a very basic function and we are just assuming that two numbers will be passed in but we can't always make those assumptions when we are writing programs.
So, let's verify that we're actually receiving numbers because if we passed in strings right now they could be concatenated together because it would just push the two strings, that would also work but that's not what we want our sum function to do 

Example: 

def sum(num1, num2):
    if (type(num1) is not int or type(num2) is not int):
        return					# we exit the function here if either arguments are not int, so it doesn't go to the next line of code inside the function.
    return num1 + num2	


total = sum('a', 3)				# changing the argument from int to str
print(total)

Output
None						# It's a special value in Python, it's not True or False, it's just None.							
########################################################################################

What happens if nothing is passed in?

def sum(num1, num2):
    if (type(num1) is not int or type(num2) is not int):
        return
    return num1 + num2


total = sum()					# here we not passing anything
print(total)

Output:
TypeError: sum() missing 2 required positional arguments: 'num1' and 'num2'
########################################################################################

We could give default values for the parameters in case if nothing is passed in as arguments.
For this example we are providing just 1 parameter as a default value.

def sum(num1, num2=3):
    if (type(num1) is not int or type(num2) is not int):
        return
    return num1 + num2


total = sum(1)					# if we pass in just 1 argument while function call, num2 will automatically have the default value that we set.
print(total)

Output:
4
########################################################################################

If the user doesn't enter any arguments, in that case we can set the default parameter value to 0, so that it doesn't come up with an error.

def sum(num1=0, num2=0):
    if (type(num1) is not int or type(num2) is not int):
        return
    return num1 + num2


total = sum()
print(total)

Output:
0
########################################################################################

In place of returning NONE when an int is not entered, we can set that to 0

def sum(num1=0, num2=0):
    if (type(num1) is not int or type(num2) is not int):
        return 0						# setting return  0 if int is not entered.
    return num1 + num2	


total = sum(1, 2)
print(total)

Output:
3
########################################################################################

If we have an unknown amount of arguments
If we have an unknown amount of arguments that will be passed into our function, we can define the parameters. We need to have just one parameter name starting with an asterisk/* sign (common practice is to use *args which is short for arguments but it can be anything) which will make the data inside the function a tuple.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

def multiple_items(*args):
    print(args)
    print(type(args))


multiple_items(1, 2, 'Sara')

Output:
(1, 2, 'Sara')
<class 'tuple'>
########################################################################################

The unknown amount of arguments have values and are represented in the parameter area. They don't have parameter names.
If we want to use keyword arguments we have to start the parameter with 2 asterisks/2 star signs. **kwargs stands for keyword arguments
Which will make the type of values as dictionary

def sum(**kwargs):
    print(kwargs)
    print(type(kwargs))


sum(first='Dave', last='Gary')

Output:
{'first': 'Dave', 'last': 'Gary'}
<class 'dict'>
########################################################################################



