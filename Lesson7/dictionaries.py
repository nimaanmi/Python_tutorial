# Dictionaries

# Dictionaries are used to store items in key and value pairs, and they are created using the {} curly brackets or braces.

# Creating a dictionary

band = {
    'vocals': 'Plant',
    'guitar': 'Page'
}

# key and value pairs are separated by :
# Each item in a dictionary is separated by a comma ,

print(band)
print(type(band))

Output:
{'vocals': 'Plant', 'guitar': 'Page'}
<class 'dict'>

# creating a dictionary using the dictionary constructor dict()

band2 = dict({'vocals': 'Plant', 'guitar': 'Page'})
print(band2)
print(type(band2))

Or

band2 = dict({
    'vocals': 'Plant', 'guitar': 'Page'
})
print(band2)
print(type(band2))

Output:
{'vocals': 'Plant', 'guitar': 'Page'}
<class 'dict'>

# creating a dictionary using the dictionary constructor dict() without the curly brackets inside the constructor.

band3 = dict(vocals='Plant', guitar='Page')        
# we are not writing the key inside quotes ' ', and the key and value pairs here are separated by = sign and not by : sign.

print(band3)
print(type(band3))

Output:
{'vocals': 'Plant', 'guitar': 'Page'}
<class 'dict'>

# Finding the length of a dictionary.

print(len(band))

Output:
2

# How to access a value in a key value pair using a key in a dictionary?

print(band['guitar'])
print(band['vocals'])

Output:
Page
Plant

# How to access/get a value in a key value pair using a key in a dictionary using a dictionary method?

print(band.get('guitar'))
print(band.get('vocals'))
# if the key is a string, write is inside '' quotes, if the key is not a string then we do not need to write it inside '' quotes.

Output:
Page
Plant

# How to list all the keys in a dictionary?

print(band.keys())

Output:
dict_keys(['vocals', 'guitar'])        # It lists all the keys inside a list.

# How to list all the values in a dictionary?

print(band.values())

Output:
dict_values(['Plant', 'Page'])

# How to list all the key value pairs / items in a dictionary as TUPLES?

band = {
    'vocals': 'Plant',
    'guitar': 'Page'
}

print(band.items())        # It prints all the key value pairs / items of a dictionary as tuples inside a list.

Output:
dict_items([('vocals', 'Plant'), ('guitar', 'Page')])        

# How to check if a key exists in a dictionary?

band = {
    'vocals': 'Plant',
    'guitar': 'Page'
}

print('guitar' in band)        # we can only checks for keys, and not values.
print('triangle' in band)

Output:

True
False

# How to change/update values in a dictionary?
# we can do this in 2 ways.

band = {
    'vocals': 'Plant',
    'guitar': 'Page'
}

#1
band['vocals'] = 'Coverdale'           # It takes just 1 argument.

print(band)

Output:
{'vocals': 'Coverdale', 'guitar': 'Page'}

#2
# band.update({'vocals': 'motels'})    # It can take as many arguement as we want.
# print(band)

Output:
# {'vocals': 'motels', 'guitar': 'Page'}

# How to add / insert key value pairs / items in a dictionary?

band = {
    'vocals': 'Coverdale',
    'guitar': 'Page'
}

#1. 
#band['mango'] = 'Tree'
#print(band)

#Output:
#{'vocals': 'Coverdale', 'guitar': 'Page', 'drums': 'Bonham', 'Mango': 'Tree'}

#2. 
band.update({'bass': 'JPJ'})    
print(band)
# It'll add / insert the key value pair at the end of the dictionary.
# we can add as many key value pairs / items as we want.

Output:
{'vocals': 'Coverdale', 'guitar': 'Page', 'bass': 'JPJ'}



# How to remove a specific item from a dictionary?

band = {
    'vocals': 'Coverdale',
    'guitar': 'Page',
    'brass': 'JPJ'
}

# print(band.pop('bass'))    # It'll return just the value and not the entire key value pair. But when we print the updated dictionary, it'll no longer have that key value pair anymore.
# print(band)

Output:
JPJ
{'vocals': 'Coverdale', 'guitar': 'Page'}

# How to remove the last entered key value pair / item?

band['drums'] = 'Bonham'    # adding a new item.
print(band)

print(band.popitem())                                        
print(band)

Output:
{'vocals': 'Coverdale', 'guitar': 'Page', 'drums': 'Bonham'}
('drums', 'Bonham')
{'vocals': 'Coverdale', 'guitar': 'Page'}


# How to delete items from a dictionary?

band = {
    'vocals': 'Plant',
    'guitar': 'Page'
}
band2 = dict({'vocals': 'Plant', 'guitar': 'Page'})

band['drum'] = 'Bonham'
print(band)
del band['drum']                                  # deletes a ke value pair.
print(band)

band2.clear()                                     # clears a dictionary.
print(band2)
del band2                                         # deletes a dictionary.

Output:
{'vocals': 'Plant', 'guitar': 'Page', 'drum': 'Bonham'}
{'vocals': 'Plant', 'guitar': 'Page'}
{}
########################################################################################

# how not to copy in dictionaries, as it creates a reference and it modifies the original dictionary

# band = {
#     'vocals': 'Plant',
#     'guitar': 'Page'
# }
# band2 = band                                    # creates a reference
# print(band2)
# print(band)

# band2['drums'] = 'Dave'
# print(band)

Output:
{'vocals': 'Plant', 'guitar': 'Page'}
{'vocals': 'Plant', 'guitar': 'Page'}
{'vocals': 'Plant', 'guitar': 'Page', 'drums': 'Dave'}
########################################################################################

# how to create copies in dictionaries

band = {
    'vocals': 'Plant',
    'guitar': 'Page'
}

band2 = band.copy()
band2['drums'] = 'Dave'
print(band2)
print(band)

Output:
{'vocals': 'Plant', 'guitar': 'Page', 'drums': 'Dave'}
{'vocals': 'Plant', 'guitar': 'Page'}
########################################################################################

# how to copy using dictionary constructor

band = {
    'vocals': 'Plant',
    'guitar': 'Page'
}

band4 = dict(band)
print(band4)

Output:
{'vocals': 'Plant', 'guitar': 'Page'}
########################################################################################

# nested dictionaries

member1 = {
    'name': 'Plant',
    'instruments': 'vocals'
}
member2 = {
    'name': 'Page',
    'instruments': 'guitar'
}
band = {
    'member1': member1,
    'member2': member2
}

print(band)
print(band['member1']['name'])                          # how to print values inside a nested dictionary.

Output:
{'member1': {'name': 'Plant', 'instruments': 'vocals'}, 'member2': {'name': 'Page', 'instruments': 'guitar'}}
Plant
########################################################################################

# how to remove duplicates and keep the original order

nums = [1, 2, 3, 6, 33, 22, 1, 2, 44, 2, 1]
nums2 = nums.copy()
nums2 = list(dict.fromkeys(nums2))
print(nums2)

Output:
[1, 2, 3, 6, 33, 22, 44]
############################################################################################
############################################################################################
############################################################################################
############################################################################################
############################################################################################
############################################################################################
############################################################################################
############################################################################################
############################################################################################

# Sets

# set is a colleciton which is unordered, unchangeable, unindexed and no duplicate members.
# It uses curly brackets like dictionary, but without key,value pairs.
# Sets prints in ascending order, doesn't allows duplicate, whichever comes first, prints it.

nums = {1, 2, 3, 4}
nums2 = set({1, 2, 3, 4})
print(nums)
print(nums2)
print(type(nums))
print(len(nums2))

Output:
{1, 2, 3, 4}
{1, 2, 3, 4}
<class 'set'>
4
########################################################################################

# no duplicates allowed.

nums = {1, 2, 2, 3}
print(nums)

Output:
{1, 2, 3}
########################################################################################

# Boolean True is 1 and False is 0

nums = {1, True, 2, False, 3, 4, 0}
print(nums)

Output:
{False, 1, 2, 3, 4}
########################################################################################

# check if a value is in a set

nums = {1, True, 2, False, 3, 4, 0}
print(2 in nums)

Output:
True
########################################################################################

# we cannot refer to an element in the set with an index position like we have with list or a key/value position like we have with dictionary but we can check if an element is present in a set.
########################################################################################

# add a new element to the set

nums = {1, True, 2, False, 3, 4, 0}
nums.add(8)
print(nums)

Output:
{False, 1, 2, 3, 4, 8}
########################################################################################

# add elements from one set to another set

nums = {1, True, 2, False, 3, 4, 0, 8}
morenums = {5, 6, 7}
nums.update(morenums)
print(nums)

Output:
{False, 1, 2, 3, 4, 5, 6, 7, 8}
########################################################################################

# we can use udpate with lists, tuples and dictionaries too. meaning, in place of passing another set in the udpate function, we can also pass a list, a tuple or a dictionary and it'll work fine.
########################################################################################

# how to merge two sets to create a new set

one = {1, 2, 3}
two = {5, 6, 7, 7, 7, 7, 7, 7, 7, 7}
mynewset = one.union(two)
print(mynewset)

Output: 
{1, 2, 3, 5, 6, 7}
########################################################################################

# keep only the duplicates in sets/ duplicate  only duplicates

one = {1, 2, 3}
two = {2, 3, 4}
one.intersection_update(two)
print(one)

Output: 
{2, 3}
########################################################################################

# keep everything except the duplicates

one = {1, 2, 3}
two = {2, 3, 4}
one.symmetric_difference_update(two)
print(one)

Output:
{1, 4}
########################################################################################

