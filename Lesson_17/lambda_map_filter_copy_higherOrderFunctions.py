Lambda and Higher Order Functions.

A lambda function is a small anonymous function that can take any number of arguments, but can only have one expression.
It cannot contain any statements, and it returns a function object which can be assigned to any variable. It is generally used for one-line expressions.

Syntax:
lambda arguments: expression

The expression is executed and the result is returned:
########################################################################################

lambda num: num * num				# lambda argument: expression
						# so we are naming the argument num, then doing multiplication expression.
						# we are not using the return keyword, but it'll return a value.

# we cannot call the lambda function into action by name because it is anonymous and doesn't have a name
# but we can assign Lambda to a variable and it will store that function into that variable

squared = lambda num: num * num			# we are assigning lambda to a variable called 'squared' and storing that function into that variable.
def squared(num): return num * num		# when we save the file, it automatically saves itself into this function format.
						# the parameter itself is the argument in lambda function.

########################################################################################

squared = lambda num: num * num

print(squared(2))

Output:
4


# Note: this will automatically will change in the VS Code. So, it's better to know both ways.

def squared(num): return num * num


print(squared(2))

Output:
4
########################################################################################

addTwo = lambda num: num + 2
print(addTwo(12))

Output:
14

# Or

def addTwo(num): return num + 2


print(addTwo(12))

Output:
14
########################################################################################

# passing more than one argument/parameters.

sum = lambda a, b: a + b
print(sum(2, 3))

Output:
5

# we could also write this as

def sum(a, b): return a + b


print(sum(2, 3))

Output:
5
########################################################################################

# when to use lambda:
# they are most often used inside of another function when we need a quick function that we don't want to save for later.

def funcBuilder(x):					# standard function with x parameter
    return lambda num: num + x				# when we return a function (like we have done in closure), we have to call the function.
							# so in this case we'll be caling the two newly build functions addTen() and addTwenty() under print() to see the output.


addTen = funcBuilder(10)				# we are using funcBuilder(x) function to build another function called addTen,, we enter 10 as argument.
addTwenty = funcBuilder(20)

print(addTen(7))					# we print the function addTen() and enter the value 
print(addTwenty(7))

Ouput: 
17
27

# So, here lambda is first being returned and then is being called when we call addTen() and addTwenty()
########################################################################################

https://www.freecodecamp.org/news/first-class-functions-and-closures-in-python/

# Higher Oder Functions:

# A higher order function is a function that takes one or more functions as arguments or a function that returns a function as its result.
Or
# A function is called Higher Order Function if it contains other functions as a parameter or returns a function as an output 

# so we'll be seeing higher order functions that accepts one or more functions as parameters when we pass those in.
# So, when we define a function we define it to accept a function as a parameter and then we actually pass in the function that function is an argument.


Example: Higher Order Function with first class functions.

def apply_operation(operation, x, y):
    return operation(x, y)

# Functions to pass as arguments
def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

# Using the higher-order function
result_add = apply_operation(add, 3, 4)
result_multiply = apply_operation(multiply, 3, 4)

print(result_add)       # Output: 7
print(result_multiply)  # Output: 12

Output:
7
12

In this example, apply_operation is a higher-order function because it takes another function (operation) as an argument. The add and multiply functions are first-class functions because they can be passed as arguments to other functions.

The apply_operation function takes three parameters: a function (operation) and two integers (x and y). It returns the result of applying the operation function to x and y.

By calling apply_operation(add, 3, 4), it returns 7, the result of adding 3 and 4. Similarly, calling apply_operation(multiply, 3, 4) returns 12, the result of multiplying 3 and 4. This demonstrates the flexibility and reusability of higher-order functions, showing how we can perform different operations on the same set of inputs.
########################################################################################

Example: Higher Order Function with first class functions.

def discount_applier(discount_rate):
    def apply_discount(price):
        return price - (price * discount_rate / 100)
    return apply_discount


# creating closures with different discount rates
holiday_discount = discount_applier(20)
member_discount = discount_applier(50)

# Applying the discount
print(holiday_discount(100))
print(member_discount(100))

Output:
80.0
50.0
########################################################################################
########################################################################################

# map() function
map is a higher order function that receives a function as the first argument and iterator/list as the 2nd argument.
It'll iterate over every item in the list, and then it'll create a new list. It'll not be a list at first, we'll have to apply the list constructor to it.

transformed = map(transformation, iterator)
# Comprehension
transformed = (transformation(x) for x in iterator)

# def map_functions(func, values):
#     return [func(value) for value in values]				# writing the code in one line

lambda num: num * num						# anonymous function
numbers = [3, 4, 5, 6, 7]					# iterator list
squared = map(lambda num: num * num, numbers)			# using in built map function and then assigning it to a variable.
# squared = (lambda(num) for num in numbers)
print(list(squared))						# we are type casting squared via the list constructor to print a new list.

Output:
[9, 16, 25, 36, 49]

#  A map function applies a given function to each item in a list (or array) and returns a new list with the results.
########################################################################################
# 2nd example:

def double(n):							# creating a function that takes n as parameter and returns a multiplication of the number
    return n * 2


def map_function(func, values):					# creating a function that takes 2 parameters [we are using first parameter as function, 2nd as list/array]
    result = []							# creating an empty list
    for value in values:					# iterating each item in the list called 'values'
        result.append(func(value))				# applying the given function 'func' to each item in the list called 'values' and appending it to the list 'result'.
    return result


# using the custom map function					
doubled_values = map_function(double, [2, 3, 4, 5, 6, 7])	# calling the map_function() and passing first argument as a function 'double', and 2nd argument as a list, and assigning it to a varible called doubled_values.
print(doubled_values)						# printing that assigned variable called doubled_values as it now acts as a function.
		
Output:
[4, 6, 8, 10, 12, 14]						# here, n * 2 = n is replaced with each item in the list as it iterates through the list, and multiplies with 2.
########################################################################################
########################################################################################

# filter() function

filter() function is a higher order function that filters the iterables/list depending on the True or False contidion of the first argument function and returns filtered items from the iterables/list.

# Iterators power and control the iteration process, while iterables typically hold data that you want to iterate over one value at a time.
# https://realpython.com/python-iterators-iterables/

filtered = filter(func, iterator)
# Comprehension
filtered = (x for x in iterator if func(x))



Example 2:
# returns True if the argument passed in is odd.
def check_odd(number):
    if number % 2 != 0:
        return True
    return False


numbers = [3, 7, 12, 18, 20, 21]

# if the element passed to check_odd() function returns True, select it.
odd_numbers = filter(check_odd, numbers)
print(list(odd_numbers))

# Output: [3, 7, 21]
########################################################################################

Example: 3:
letters = ['a', 'b', 'd', 'e', 'i', 'j', 'o']

# a function that returns True if letter is vowel
def filter_vowels(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if letter in vowels:
        return True 
    else:
        return False

# selects only vowel elements
filtered_vowels = filter(filter_vowels, letters)

# converting to tuple
vowels = tuple(filtered_vowels)
print(vowels)

# Output: ('a', 'e', 'i', 'o')
########################################################################################
########################################################################################

reduce()

from functools import reduce

https://www.geeksforgeeks.org/program-compute-division-upto-n-decimal-places/

The reduce(fun,seq) function is used to apply a particular function passed in its argument to all of the list elements mentioned in the sequence passed along.This function is defined in “functools” module.

Working :  

At first step, first two elements of sequence are picked and the result is obtained.
Next step is to apply the same function to the previously attained result and the number just succeeding the second element and the result is again stored.
This process continues till no more elements are left in the container.
The final returned result is returned and printed on console.

Example1: 

# python code to demonstrate working of reduce()

# importing functools for reduce()
import functools

# initializing list
lis = [1, 3, 5, 6, 2]

# using reduce to compute sum of list
print("The sum of the list elements is : ", end="")
print(functools.reduce(lambda a, b: a+b, lis))

# using reduce to compute maximum element from list
print("The maximum element of the list is : ", end="")
print(functools.reduce(lambda a, b: a if a > b else b, lis))

Output
The sum of the list elements is : 17
The maximum element of the list is : 6
########################################################################################

Example2: 

def total_sum(x, y):
    return x - y


list1 = [2, 1, 1, 1, 1, 1, 2]
total = reduce(total_sum, list1)
print(total)

Output:
-5
########################################################################################
Eaxmple3: 

numbers = [1, 2, 3, 4, 5, 1]
total = reduce(lambda a, b: a + b, numbers)
print(total)

Output: 
16

# we could also start from a different value.

numbers = [1, 2, 3, 4, 5, 1]
total = reduce(lambda a, b: a + b, numbers, 10)
print(total)

Output:
26
########################################################################################
We could use a different function to compute the same above problem in a more simpler way.

numbers = [1, 2, 3, 4, 5, 1]
print(sum(numbers))						

Output:
16
########################################################################################

We could also inside the sum function from a different value.

numbers = [1, 2, 3, 4, 5, 1]
print(sum(numbers, 10))						

Output: 
26
########################################################################################

names = ['Gary Dave', 'Sara Ito', 'Ino ano lang saan']
total = reduce(lambda acc, cur: acc + len(cur), names, 0)				
print(total)

Output:
34

# here we do not have the optional starting value as we are using string, but we want to tell reduce() that we are going to be using numbers if not it would view this as a string that was trying to add number two and we would get a type error back. So, we put in the starting value of 0 
########################################################################################

The operator Module:

As has been shown in a few of the examples, every operation that can be done with Python’s infix and prefix operators corresponds to a named function in the operator module. For places where you want to be able to pass a function performing the equivalent of some syntactic operation to some higher-order function, using the name from operator is faster and looks nicer than a corresponding lambda. For example:

# Compare ad hoc lambda with `operator` function
sum1 = reduce(lambda a, b: a+b, iterable, 0)
sum2 = reduce(operator.add, iterable, 0)
sum3 = sum(iterable)    # The actual Pythonic way
########################################################################################



