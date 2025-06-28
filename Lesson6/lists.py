
Arrays / Data Structures: 
In python arrays are called data structures or collections which refer to container data types that are used to store and organize multiple itmes or values.

# Python collections (Arrays)  [Array starts with 0 and not 1]
# There are 4 collection data types in the Python programming language:
1. List              List is a collection which is ordered and changeable. Allows duplicate members
2. Tuple             Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
3. Set               Set is a collection which is unordered, unchangeable, and unindexed. No duplicate members.
4. Dictonary         Dictonary is a collection which is ordered and changeable. No duplicate members.   
############################################################################################

List
A list is a data structure in python that is changeable, ordered sequence of elements within a square bracket, each element or values inside a list is called an item.

Lists are created using square brackets:

users = ['Dave', 'John', 'Sara']
data = ['Dave', 42, True]                         # List is not limited to string data type or anyone data type. 
emptylist = []                                    # we can also have empty list.

# How to check if a value/item is present inside a list or not?

print('Dave' in users)               We use in / not in membership operator.
print('Dave' in data)
print('Dave' in emptylist)
print(users)

Output:
True
True
False
['Dave', 'John', 'Sara']
############################################################################################

# How to get a specific item/value from a list and we know what position it is in. Remember, lists starts with 0 index.

users = ['Dave', 'John', 'Sara']

print(users[0])                      # prints the first item in the list.
print(users[1])                      # prints the second item in the list.
print(users[2])                      # prints the third item in the list.
print(users[-1])                     # prints the last item in the list.
# Use the [] Bracket Notation.
# list indices must be integers or slices, not str

Output:
Dave
John
Sara
Sara

# How to get the position/index of an item/value in a list?

print(users.index('Dave'))          # use the list method called index()
print(users.index('John'))
print(users.index('Sara'))

Output:
0
1
2

# How to check or get a range of values in a list?

print(users[:])                    # prints all the items in the list.
print(users[0:])                   # prints all the items in the list from the first position.
print(users[1:2])                  # prints the items from index 1 but excludes index 2.
print(users[0:2])                  # prints all the items from index 0 but excludes the index 2.
print(users[-3:-1])                # we can also use negative, -1 is the last position, -2 before that and so on. Again, it'll exclude the -1 index.

Output:
['Dave', 'John', 'Sara']
['Dave', 'John', 'Sara']
['John']
['Dave', 'John']
['Dave', 'John']

# How to find the length of a list?

print(len(users)) 

Output:
3
############################################################################################

# Adding an item to an existing list. 

users = ['Dave', 'John', 'Sara']

users.append('Elsa')              
print(users)
# append() method takes exactly one argument, nothing more. By deafult it'll be added to the end of the list.

Output:
['Dave', 'John', 'Sara', 'Elsa']

# Adding an existing list to a new list.

users += ['Jason']                
print(users)    
# we can add as many items as we want as long as it's inside the [].
# make sure to use the [] while creating the list, if we miss [] and just use 'Jason', it'll add each letter as an item.
# 1st list = users, 2nd list just created has one time called 'Jason'. So, here we have created a new list and add added to another list.

Output:
['Dave', 'John', 'Sara', 'Elsa', 'Jason']

# Another way of adding an existing list while creating a new list

users.extend(['Robert', 'Jimmy'])                        
print(users)
# We can have as many items as we want as long as it's within the [] within the extend() mehtod parenthesis.  
# If we do not use the [], even extend() method takes just 1 argument, nothing more. And it'll take each letter as an item.

Output:
['Dave', 'John', 'Sara', 'Elsa', 'Jason', 'Robert', 'Jimmy']

# Passing pre existing list to a new list.

data = ['Dave', 42, True] 
#users.extend(data)                                     # we can also add pre existing list to the current list
#print(users)
# It adds the 2nd  list to be back of the first list.
# Use the append() method to add just 1 item in a list, apart from that always use the extend() method for more.

Output:
#['Dave', 'John', 'Sara', 'Elsa', 'Jason', 'Robert', 'Jimmy', 'Dave', 42, <class 'bool'>]

# Adding or inserting items to a specific position in a list.

users.insert(0, 'Bob')                                  # we can add the items anywhere in the list.
print(users)
# Inside the insert() list method, the first argument is the index number, and the second argument is the item name.

Output:
['Bob', 'Dave', 'John', 'Sara', 'Elsa', 'Jason', 'Robert', 'Jimmy']

# Adding or inserting more than 1 item in a list at a specific position without replacing the existing item.
# we use [] bracket notation and make sure that the starting and ending index are same.

users[2:2] = ['Eddie', 'Alex']                          # We could choose 4:4 or 7:7
print(users)

Output: 
['Bob', 'Dave', 'Eddie', 'Alex', 'John', 'Sara', 'Elsa', 'Jason', 'Robert', 'Jimmy']

# How to replace items in a list?

users[1:3] = ['Roberts', 'JPJ']                         # it replaces indexes 1 and 2 excluding index 3, since the ending value is always excluded in a range. 
print(users)

Output:
['Bob', 'Robert', 'JPJ', 'Alex', 'John', 'Sara', 'Elsa', 'Jason', 'Robert', 'Jimmy']

# How to remove items from a list?

users.remove('Bob')                                     
print(users)
# We can also use index to remove an item from a list. || users.remove(users[1]) || It'll remove Robert from index 1.
# However, remove() method does not take a range of indexes.

Output: 
['Robert', 'JPJ', 'Alex', 'John', 'Sara', 'Elsa', 'Jason', 'Robert', 'Jimmy']

# How to pop off the last user or item from a list?

print(users.pop())
print(users)
# The pop method will return that value even though it removes it from the list.

Output:
Jimmy
['Robert', 'JPJ', 'Alex', 'John', 'Sara', 'Elsa', 'Jason', 'Robert']

# How to remove or delete a specific user or item from a list?
# we use the keyword del which stands for delete.

del users[0]                                           
print(users)
# we can also select a range of indexex to delete eg: [0:4]

Output:
['JPJ', 'Alex', 'John', 'Sara', 'Elsa', 'Jason', 'Robert']

# We can also delete a list completely.

#del data                                               # we can also delete a complete data list
#print(data)

Output:
NameError: name 'data' is not defined

# How to clear or empty a list without deleting the list?

data.clear()
print(data)

Output: 
[]
############################################################################################

# Sorting a list.

users = ['Jimmy', 'Alex', 'John', 'Sara', 'Elsa', 'Jason', 'Robert']
data = []

print(users)

#users.sort()           # It sorts alphabetically
#print(users)

Output:
['Alex', 'Elsa', 'JPJ', 'Jason', 'John', 'Robert', 'Sara']

# sorting sorts alphabetically a to z. However, capital letters comes first before small letters. So, replace the first index with 'dave' and then sort it again.
users[1:2] = ['dave']
users.sort()
print(users)

Output:
['Elsa', 'JPJ', 'Jason', 'John', 'Robert', 'Sara', 'dave']

# Sorting with small letters first and then capital letters.

users.sort(key=str.lower)                              
print(users)

Output:
['dave', 'Elsa', 'Jason', 'Jimmy', 'John', 'Robert', 'Sara']

# Sorting only works on same data types. It wouldn't work on different data types.
############################################################################################

nums = [4, 42, 78, 1, 5]

nums.reverse()                                           # reversing the list from end to start
print(nums)

#nums.sort()                                             # sorting from lowest number to highest number in list
#print(nums)

#nums.sort(reverse=True)                                  # sorting integers from highest to lowest in list
#print(nums)

print(sorted(nums, rerverse=True))                       # how to keep the original list and do the sorting using global variable.
print(nums)

Output:
[5, 1, 78, 42, 4]
#[1, 4, 5, 42, 78]
#[78, 42, 5, 4, 1]
[5, 1, 78, 42, 4]
############################################################################################

# how to take a copy of the original list and sort without changing the original list.
# we can do this in three different ways.

nums = [4, 42, 78, 1, 5]
numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

print(numscopy)					                                  # we just displaying the copied version of the original list.
print(sorted(mynums, reverse=True))		                    # we are using global sorting and reversing the original list and displaying the copy.
print(sorted(mycopy))				                              # we are using global sorting and displaying the copy.
print(nums)					                                      # we are just displaying the original list.

Output:
[1, 4, 5, 41, 78]
[78, 41, 5, 4, 1]
[1, 4, 5, 41, 78]
[5, 1, 78, 41, 4]
############################################################################################

nums = [4, 42, 78, 1, 5]

print(type(nums))

Output:
<class 'list'>
############################################################################################

mylist = list([1, 'Neil', True])		# creating a list in a different way
print(mylist)

Output:
[1, 'Neil', True]
############################################################################################
############################################################################################

Tuple
Tuples are very much like List, except the data inside the Tuples will not change, and the order the data is in will not change.

A list contains a sequence of data surrounded by square brackets.
A tuples contains a list of data surrounded by round brackets / parentheses.

nums = (1, 4, 2, 8)
print(nums)
print(type(nums))

Output:
(1, 4, 2, 8)
<class 'tuple'>
############################################################################################

newnums = tuple((1, 'Neil', True))                              # creating a tuple using the tuple constructor
print(newnums)
print(type(newnums))

Output:
(1, 4, 2, 8)
<class 'tuple'>
############################################################################################

# How to check the memory and size of an objet?
import sys

list_eg = [1, 2, 3, 'a', 'b', 'c', True, 3.14159]               # list
tuple_eg = (1, 2, 3, 'a', 'b', 'c', True, 3.14159)              # tuple

print('List size = ', sys.getsizeof(list_eg))
print('Tuple size = ', sys.getsizeof(tuple_eg))

Output:
List size =  120
Tuple size =  104
############################################################################################

tuple_eg2 = (1, 4, 2, 8)
(one, two, *hey) = tuple_eg2                                      # How to unpack the tuple
print(one)                                                        # it holds the first value
print(two)                                                        # it holds the 2nd value
print(hey)                                                        # it holds the rest of the values,, where ever we have * holds the rest of the values

Output:
1
4
[2, 8]
############################################################################################

tuple_eg2 = (1, 4, 2, 8, 2, 3, 2, 2, 2)
print(tuple_eg2.count(2)                                          # we are trying to check how many times number 2 is used.

Output:
5
############################################################################################

# how to check the time taken by an object?
import timeit

list_test = timeit.timeit(stmt='[1, 2, 3, 4, 5]', number=1000000)
tuple_test = timeit.timeit(stmt='(1, 2, 3, 4, 5)', number=1000000)

print('List test: ', list_test)
print('Tuple test: ', tuple_test)

Output:
List test:  0.07566610001958907                                   # it takes more time for a list.
Tuple test:  0.015406199963763356
############################################################################################

test1 = ('a')
print(test1)

test2 = ('a', )
print(test2)

Output:
a				                             # If we use just one character/word, it'll print it as a string.
('a',)				                       # if we do not want it to print it as a string, we need to add a comma at the end of the tuple.
############################################################################################

# We could also print tuples without using round brakcets / parentheses

test1 = 1,
test2 = 1, 2,
test3 = 1, 2, 3,

print(test1)
print(test2)
print(type(test3))

Output:
(1,)
(1, 2)
<class 'tuple'>
############################################################################################

# tuples assisnment or tuples with 1 element

survey = (21, 'Srilanka', False)
age, country, knows_python = survey

print('Age: ', age)
print('Country: ', country)
print('Knows Python? ', knows_python)

Output:
Age:  21
Country:  Srilanka
Knows Python?  False
     
