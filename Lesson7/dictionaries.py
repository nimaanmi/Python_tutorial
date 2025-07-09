# Dictionaries

# Dictionaries are used to print values in pairs and are represented by braces or curly brackets.
# They come as key and value.

# different ways of creating a dictionary
band = {
    'vocals': 'Plant',
    'guitar': 'Page'
}

band2 = dict({'vocals': 'Plant', 'guitar': 'Page'})
band3 = dict(vocals='Plant', guitar='Page')

print(band)
print(band2)
print(band3)
print(len(band))
print(type(band))

Output:
{'vocals': 'Plant', 'guitar': 'Page'}
{'vocals': 'Plant', 'guitar': 'Page'}
{'vocals': 'Plant', 'guitar': 'Page'}
2
<class 'dict'>
########################################################################################

# how to access items in dictionaries?

band = {
    'vocals': 'Plant',
    'guitar': 'Page'
}

print(band['guitar'])
print(band.get('vocals'))

Output:
Page
Plant
########################################################################################

# dictionaries are key and value pairs.
# list all keys in dictionaries

band = {
    'vocals': 'Plant',
    'guitar': 'Page'
}

print(band.keys())

Output:
dict_keys(['vocals', 'guitar'])
########################################################################################

# dictionaries are key and value pairs.
# list all values in dictionaries

band = {
    'vocals': 'Plant',
    'guitar': 'Page'
}

print(band.values())

Output:
dict_values(['Plant', 'Page'])
########################################################################################

# list of all key and value pairs as TUPLES.

band = {
    'vocals': 'Plant',
    'guitar': 'Page'
}

print(band.items())

Output:
dict_items([('vocals', 'Plant'), ('guitar', 'Page')])
########################################################################################

# verify if a key exists in a dictionary

band = {
    'vocals': 'Plant',
    'guitar': 'Page'
}
band2 = dict({'vocals': 'Plant', 'guitar': 'Page'})

print('guitar' in band)
print('triangle' in band2)

Output:

True
False
########################################################################################

# how to change values in dictionaries

band = {
    'vocals': 'Plant',
    'guitar': 'Page'
}

band['vocals'] = 'Coverdale'
band.update({'bass': 'JPJ'})
print(band)

Output:
{'vocals': 'Coverdale', 'guitar': 'Page', 'bass': 'JPJ'}
########################################################################################

# # remove items from dictionaries

# band = {
#     'vocals': 'Plant',
#     'guitar': 'Page',
#     'bass': 'JPJ'
# }

# print(band.pop('vocals'))
# print(band)

# Output:
# Coverdale
# {'guitar': 'Page', 'bass': 'JPJ'}
########################################################################################

# remove items from dictionaries

band = {
    'vocals': 'Plant',
    'guitar': 'Page',
    'bass': 'JPJ'
}

print(band.pop('bass'))
print(band)

band['drums'] = 'Bonham'
print(band)

print(band.popitem())                                        # remove the last entered item/ key,value pair, in this case drums: Bonham
print(band)

Output:
JPJ
{'vocals': 'Plant', 'guitar': 'Page'}
{'vocals': 'Plant', 'guitar': 'Page', 'drums': 'Bonham'}
('drums', 'Bonham')
{'vocals': 'Plant', 'guitar': 'Page'}
########################################################################################

# delete and clear items in dictionaries

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

