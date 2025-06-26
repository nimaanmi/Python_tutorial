
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

# How to check if a value/item is present inside a list or not?  We use in / not in membership operator.

print(users)
print('Dave' in users)
print('Dave' in data)
print('Dave' in emptylist)

Output:
['Dave', 'John', 'Sara']
True
True
False
############################################################################################

# How to get a specific item/value from a list and we know what position it is in. Remember, lists starts with 0 index.

users = ['Dave', 'John', 'Sara']

print(users[0])                      # prints the first item in the list.
print(users[1])                      # prints the second item in the list.
print(users[2])                      # prints the third item in the list.
print(users[-1])                     # prints the last item in the list.

Output:
Dave
John
Sara
Sara

# How to get an index/position of an item/value?

print(users.index('Sara'))          

Output:
2

# How to check a range of values?

print(users[0:])                     # prints all the times in the list from the first position.
print(users[:2])                     # pritns the items from first position to 2nd postion, (excludes the thirst as it's inclusive)
print(users[-3: -1])                 # we can also use negative, -1 is the last position, -2 before that and so on.

Output:
['Dave', 'John', 'Sara']
['Dave', 'John']
['Dave', 'John']

# How to find the length ofa list?

print(len(users)) 

Output:
3
############################################################################################

users = ['Dave', 'John', 'Sara']
data = ['Dave', 42, True]

users.append('Elsa')                                    # how to add a single item to an existing list, it'll be added at the last.
print(users)

users += ['Jason']                                      # we can also create a new list and add it to the list
print(users)

users.extend(['Roert', 'Jimmy'])                        # we can add new items to the list this way too. It allows to add more then 1 item.
print(users)

#users.extend(data)                                     # we can also add pre existing list to the current list
#print(users)

users.insert(0, 'Bob')                                  # we can add the items anywhere in the list.
print(users)

users[2:] = ['Eddie', 'Alex']                           # how to add items in the list anywhere || without replacing the existing item.. We could choose 4:4 or 7:7
print(users)

users[1:3] = ['Roberts', 'JPJ']                         # how to replace items from the list || here it replaces excluding 0 from 1 till 2. 
print(users)

users.remove('Bob')                                     # how to remove items from the list by using index/item names
print(users)

users.pop()                                             # how to remove the last item from the list
print(users)

del users[0]                                            # how to delete/remove item using index number  || we can also give a range of index [0:4]
print(users)

#del data                                               # we can also delete a complete data list
#print(data)

data.clear()
print(data)

Output:
['Dave', 'John', 'Sara', 'Elsa']
['Dave', 'John', 'Sara', 'Elsa', 'Jason']
['Dave', 'John', 'Sara', 'Elsa', 'Jason', 'Robert', 'Jimmy']
#['Dave', 'John', 'Sara', 'Elsa', 'Jason', 'Robert', 'Jimmy', 'Dave', 42, True]
['Bob', 'Dave', 'John', 'Sara', 'Elsa', 'Jason', 'Robert', 'Jimmy']
['Bob', 'Dave', 'Eddie', 'Alex', 'John', 'Sara', 'Elsa', 'Jason', 'Robert', 'Jimmy']
['Bob', 'Robers', 'JPJ', 'Alex', 'John', 'Sara', 'Elsa', 'Jason', 'Robert', 'Jimmy']
['Robert', 'JPP', 'Alex', 'John', 'Sara', 'Elsa', 'Jason', 'Robert', 'Jimmy']
['Robert', 'JPP', 'Alex', 'John', 'Sara', 'Elsa', 'Jason', 'Robert']
['Jimmy', 'Alex', 'John', 'Sara', 'Elsa', 'Jason', 'Robert']
#NameError: name 'data' is not defined
[]
############################################################################################

users = ['Jimmy', 'Alex', 'John', 'Sara', 'Elsa', 'Jason', 'Robert']
data = []

print(users)

#users.sort()                                            # It sorts alphabetically
#print(users)

# sorting takes caps letter first then the small letters by default || here we replaced the first index with dave and then sorted it.
users[1:2] = ['dave']
users.sort()
print(users)

users.sort(key=str.lower)                                # how to sort from lowered letters to caps letters alphabetically.
print(users)

Output:
Output:
#['Alex', 'Elsa', 'Jason', 'Jimmy', 'John', 'Robert', 'Sara']
['Elsa', 'Jason', 'Jimmy', 'John', 'Robert', 'Sara', 'dave']
['dave', 'Elsa', 'Jason', 'Jimmy', 'John', 'Robert', 'Sara']
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
     
