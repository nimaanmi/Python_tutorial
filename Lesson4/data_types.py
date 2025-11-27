How to name a file in python. 
We always use small letters. To separate words we use underscore.. So, data_types.py
####################################################################################

# Data types: 

The first data type is the String data type
In Python, the string data type, abbreviated as str, represents sequences of characters and is used for handling textual data.

# literal assignment
We are literally assigning values to variables.

first = 'Dave'
last = 'Gary'
message = 42

print('')                              # prints an empty line.
print(first)                           # prints the assigned value of the object 'first'.
print(message)                         # prints the assigned value of the object 'message'.
print(type(first))                     # Checks the data type of the object 'first' and then prints the data type.
print(type(message))                   # Checks the data type of the object 'message' and then prints the data type.
print(type(first) == str)              # Checks the data type of the object 'first', and also checks if it's a str then prints a boolean value.
print(type(message) == str)            # Checks the data type of the object 'message', and also checks if it's a str then prints a boolean value.
print(isinstance(first, str))          # Checks if the object 'first' is an instance of the data type str and then prints a boolean value.
print(isinstance(message, int))        # Checks if the object 'message' is an instance of the data type str and then prints a boolean value.
print(isinstance(message, str))        # Checks if the object 'message' is an instance of the data type str and then prints a boolean value.


Output: 
Dave
42
<class 'str'>
<class 'int'>
True
False
True
True
False
#######

type()
The type() function is used to print the data type of an object.

message = 42
print(type(messge))

Ans: <class 'int'>	<-- prints the class as integer.
#######

isinstance()
The isinstance() function is used to test if an object is an instance of a specified data type.
This will print a boolean value for each function call, indicating if the object is an instance of the given type:

word = "purple"
languages = ("Python", "JavaScript", "Go")

print(isinstance(word, str)) # Output: True
print(isinstance(languages, list)) # Output: False
print(isinstance(languages, tuple)) # Output: True

####################################################################################

Constructor function:
Another way of assigning values is by using the constructor fucntion str() while creating an object/variable.
We can do this for other data types as well, i.e., int(), float(), bool() 

pizza = str('Pepperoni')
print(type(pizza))
print(type(pizza) == str)
print(isinstance(pizza, str))

Output:
<class 'str'>
True
True
####################################################################################

How to replace words.

Highlight a word, Ctrl+D (can press a few times if more same words needs to be replaced) and write the new word. Done.
####################################################################################

Concatenation
Adding two strings to form a larger string. This is not a mathematical addition but just joining two objects.

first = 'Dave'
last = 'Gary'
fullname = first + " " + last
print(fullname)

Output:
Dave Gary

fullname += '!'
print(fullname)

Output:
Dave Gary!
####################################################################################

Casting a number to a string
decade = str(1980)
print(type(decade))
print(decade)

Output:
<class 'int'>
1980

statement = 'I like rock music from the ' + decade + 's.'      # if we want to concatinate the value inside of a sentence, we'll need to caste the number to a string.
print(statement)

Output:
I like rock music from the 1980s.
####################################################################################

Multiple lines                      We use '''''' 6 single apostrophe write the sentences in the middle of the apostrophes, which is after 3 apostrophes.

multiline = '''
Hey, how are you?
    I was just checking in.
                                All good?

'''
print(multiple)

Output:
Output:
Hey, how are you?
    I was just checking in.
                                All good?

####################################################################################

Escaping special characters

# adding a backward slash lets the program know that you are adding ' after it, so it doens't cause issue with the '' single apostrophones for that string.
sentence = 'I\'m back'		
print(sentence)

Output:
I'm back

sentence = 'I\'m back at work!\tHey'	#the second backward slash \t followed by t is used to add a tab space in the sentence.
print(sentence)

Output:
I'm back at work!       Hey.

sentence = 'I\'m back at work!\tHey\n\nWhere\'s this'	# \n is used to add a new line, we can use it as many times as we want \n\n\n\n\n...
print(sentence)

Output:
I'm back at work!       Hey

Where's this

sentence = 'I\'m back at work!\tHey\n\nWhere\'s this at\\located?'	# if we want a \ to be shown inside a sentence, we'll have to use it twice.
print(sentence)

Output: 
I'm back at work!       Hey

Where's this at\located?
####################################################################################

String Methods

Methods and functions have similar purposes. Functions are independent blocks of code that can called from anywhere. While, methods are tied to objects or classes and needs an object or class instance to be invoked.

first = 'Dave'
print(first)
print(first.upper())              #.upper() is a method, here it makes all the characters in capital letter
print(first.lower())
print(first)

Output:
Dave
DAVE
dave
Dave


multiline = '''
Hey, how are you?
    I was just checking in.
                            All good?
                            
'''
print(ultiline.title())
print(multiline.replace('good', 'bad'))
print(multiline)

Output:
Hey, how are you?
    I was just checking in.
                            All good?

Hey, How Are You?
    I Was Just Checking In.
                            All Good?

Hey, how are you?
    I was just checking in.
                            All bad?

Hey, how are you?
    I was just checking in.
                            All good?


print(len(multiline))
multiline += "     "		# added 5 spaces  	<-- we can do the same thing in a different way in the below line.
multiline = "     " + multiline  # added 5 more spaces 
print(len(multiline))

Output:
86
96
####################################################################################

How to remove white spaces?

yourName = input('What is your name? ')
print("Hello, " + yourName)

Output: 
What is your name? Itachi
Hello, Itachi
#########

1. name01 = "   This   is   a strong      sentence !!! "
print(name01)
   This   is   a strong      sentence !!!               # it prints all the spaces.

2. name01 = name01.strip()
print(name01)
This   is   a strong      sentence !!!                  # removes the starting and ending white spaces.

3. name01 = name01.rstrip()
print(name01)
   This   is   a strong      sentence !!!               # only removes the right end white spaces.

4. name01 = name01.lstrip()
print(name01)
This   is   a strong      sentence !!!                  # only removes the left end white spaces.

4. import re
name01 = re.sub(" +", " ", name01)
print(name01)
   This is a strong sentence !!!                         # removes the white spaces between words, keeping just 1 space between them but not the starting and ending of the sentences.

5. import re
name01 = re.sub(" +", " ", name01).strip()
This is a strong sentence !!!                           # removes all the white spaces keeping just 1 space between words

6. name01 = name01.replace(" ", "")
print(name01)
Thisisastrongsentence!!!                                # removes all the white spaces completely.
####################################################################################

# Build a menu

title = 'menu'.uppler()
print(title.center(20, "="))

Output:
========MENU========                                    # it consists of a total of 20 characters including the strings MENU. 

title = 'menu'.upper()
print(title.center(20, '='))
print('coffee'.ljust(16, '.') + '$1'.rjust(4, ' ')      
                          # we have left the string part in .rjust() empty so the outcome has empty spaces. If we want we can fill that too as done in .ljust()

Output:
coffee..........  $1

title = 'menu'.upper()
print(title.center(20, '='))
print('Coffee'.ljust(16, '.') + '$1'.rjust(4, ' '))
print('Muffin'.ljust(16, '.') + '$1'.rjust(4, ' '))
print('Cheesecake'.ljust(16, '.') + '$1'.rjust(4, ' '))

Output:
Coffee..........  $1
Muffin..........  $2
Cheesecake......  $4
####################################################################################

String index values

import re

first = 'Dave is a great    tutor'
first = re.sub(" +", " ", first)	              # we are making sure that there are no white spaces.
print(first[1])				                          # it prints the second letter, as Array starts with 0
print(first[0])				                          # it prints the first letter, as Array starts with 0
print(first[1:-1])			                        # it prints from 2nd letter and unto last second letter <-- so not a good idea using this code
print(first[1:])			                          # it prints from the 2nd letter to the last letter.
print(first[0:])			                          # it prints from first letter to last letter

Output:
a
D
ave is a great    tuto
ave is a great    tutor
Dave is a great    tutor
####################################################################################

Some methods return boolean data

import re

first = 'Dave is a great      tutor       '
first = re.sub(' +', ' ', first).strip()        # just for practice for white spaces.

print(first.startswith('D'))    		            # If the strings variable starts with D, it'll print True
print(first.endswith('Z'))                      # If the strings variable ends with Z, it'll print True, if not false.

Ouput:
True
False
####################################################################################

Boolean data type

myvalue = True
x = bool(False)
print(type(x))
print(isinstance(myvalue, bool))

Output:
<class 'bool'>
True
####################################################################################

Numeric data types

price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))

Output:
<class 'int'>
True
####################################################################################

float type

gpa = 3.28
y = float(1.14)
print(type(gpa))

Output:
<class 'float'>
####################################################################################

complex type                            # it's often used in electrical engineering.

comp_value = 5+3j                        # here 5 is a real value and 3 is an imaginary value
print(type(comp_value))
print(int(comp_value.real))
print(comp.value.imag)

Output:
<class 'complex'>
5
3.0
####################################################################################

Built in functions for numbers

gpa = 3.28

print(abs(gpa))                      # checks/prints the absolute value
print(abs(gpa * 4))                  # multiplies the value of gpa into 4
print(abs(gpa * -1)                  # it'll not print a negative value, that's how absoulute works.
print(round(gpa))                    # it'll round up the value to to the nearest integer value
print(round(gpa, 1))                 # it'll round up the the nearest decimal value.

Output:
3.28
13.12
3.28
3
3.3

import math

print(math.pi)                      # prints the value of pi
print(math.sqrt(64))                # prints the square root of 64 in float
print(int(math.sqrt(64)))           # prints the square root of 64 in int
print(math.ceil(gpa))               # prints the ceiling/next integer value
print(math.floor(gpa))              # prints the floor/previous or existing integer value

Output:
3.141592653589793
8.0
8
4
3
####################################################################################  

Casting a string to a number

zipcode = '10001'
zip_value = int(zipcode)
print(type(zip_code))

Output:
<class 'int'>
#################################################################################### 

Python String count() Method

# The count() method in Python returns the number of times a specified substring appears in a string.
# It is commonly used in string analysis to quickly check how often certain characters or words appear.

s = "hello world"
res = s.count("o")
print(res)

Output:
2                                    # Because o is found twice in the string s.

Counting Words in String

s = "Python is fun and Python is powerful."
print(s.count("Python"))

Output: 
2                                    # Because the word Python is written twice in the string s

Count Substring Occurrences with Start and End parameter

s = "apple banana apple grape apple"
substring = "apple"

# Using start and end parameters to count occurrences 
# of "apple" within a specific range
res = s.count(substring, 1, 20)  
print(res)

Output: 
1                                    # Because the world 'apple' is found once from the index 1 to index 20. 
#################################################################################### 





