Lesson13

f-strings

Python f-strings provide a quick way to interpolate and format strings. They’re readable, concise, and less prone to error than traditional string interpolation and formatting tools, such as the .format() method and the modulo operator (%). An f-string is also a bit faster than those tools!


person = 'dave'
coins = 3
message = '\n%s has %s coins left.' % (person, coins)
print(message)

person = 'Dave'
coins = 4
message = '\n%s has %s coins left.' % (person, coins)
print(message)

Output:
dave has 3 coins left.

Dave has 4 coins left.
########################################################################################

We can also write the above details as

person = 'River'
coins = 100
message = '\n{} has {} coins left.'.format(person, coins)
print(message)

Output:
River has 100 coins left.
########################################################################################
We can also flip the arguments inside the format() method and accordingly enter the indexes inside the curly brackets.

person = 'River'
coins = 13
message = '\n{1} has {0} coins left.'.format(coins, person)
print(message)

Output:
River has 13 coins left.

# we cannot essentially track the order of these if we want to flip them around and then insert the values by which they are as far
# as the index inside of the format method remember we can do that rememer the index starts with 0 so we have
########################################################################################

We can also assign the arguments inside the .format() method and enter those new variables inside the curly brackets.

person = 'Dave'
coins = 3
message = '\n{person} has {coins} coins left.'.format(coins=coins, person=person)
print(message)

Output
Dave has 3 coins left.
########################################################################################

we can also call the key from a dictionary and it'll print the value

player = {'person': 'sam', 'coins': 4}
message = '\n{person} has {coins} coins left.'.format(**player)
print(message)

Output:
sam has 4 coins left.
########################################################################################

f-string starts from here

The reason we use f-strings is because if we use %s, we may have to use a lot of it.
Also, if we use the .format(), and we want to add more arguments, we'll have to write a lot of time and then entering it into the {}, the code becomes lengthy.

To avoid the confusion and the lengthy code we use f-strings.

person = 'Shastri'
coins = 113
message = f'\n{person} has {coins} coins left.'
print(message)

Output:
Shastri has 113 coins left.
########################################################################################

We can also write down any calculations inside the curly brackets in place of re-writing the assigned variables.

person = 'tom'
message = f'\n{person} has {3*6} coins left.'
print(message)

Output:
tom has 18 coins left.
########################################################################################

We can also use methods inside of {} curly brackets of f-strings.

person = 'Dave'
message = f'\n{person.lower()} has {coins} coins left.'
print(message)

Output:
dave has 4 coins left.
########################################################################################

if we use the dictionary > key, inside the {} curly brackets we'll have to use single quote if the f-string is double quotes, or use double quotes if the f-string is single quote

player = {'person': 'Dave', 'coins': 4}
message = f'\n{player["person"]} has {player["coins"]} coins left'
print(message)

Output:
Dave has 4 coins left.
########################################################################################

# we can pass formatting options.

Formatting starts with : (colon), says how to format it.

num = 9
print(f'\n2.25 times {num} is {2.25 * num:.2f}')

Output:
2.25 times 9 is 20.25

After the : .2 is used to put 2 numbers after the decimal and the 'f' stands for fixed.
########################################################################################

We can also put this into a loop.

for i in range(1, 11):
    print(f'10 times {i} is {10 * i:.2f}')

Output:
10 times 1 is 10.00
10 times 2 is 20.00
10 times 3 is 30.00
10 times 4 is 40.00
10 times 5 is 50.00
10 times 6 is 60.00
10 times 7 is 70.00
10 times 8 is 80.00
10 times 9 is 90.00
10 times 10 is 100.00
########################################################################################

We can also find the percentage within the for loop.

for num in range(1, 11):
    print(f'{num} divided by 2 is {num / 2:.2%}')

Output:
1 divided by 2 is 50.00%
2 divided by 2 is 100.00%
3 divided by 2 is 150.00%
4 divided by 2 is 200.00%
5 divided by 2 is 250.00%
6 divided by 2 is 300.00%
7 divided by 2 is 350.00%
8 divided by 2 is 400.00%
9 divided by 2 is 450.00%
10 divided by 2 is 500.00%
########################################################################################
########################################################################################
########################################################################################

https://www.w3schools.com/python/ref_string_format.asp

We can try out all the possible formatting options from here.

# :< left aligns the result within the available space.

num = 5
message = f'We have {num:<10} chickens.'
print(message)

Output:
We have 5          chickens.
########################################################################################

# :> right aligns the result within the available space.

num = 10
message = f'We have {num:>8} chickens.'
print(message)

Output:
We have       10 chickens.
########################################################################################

# Use "^" to center-align the value:

num = 13
message = f'We have {num:^8} chickens.'
print(message)

Output:
We have    13    chickens.
########################################################################################

# := Places the sign to the left most position

num = -1
message = f'The temperature is {num:=4} degree celsius.'
print(message)

Output:
The temperature is -  1 degree celsius.

# it counts from 1, then - sign place is 2, if we enter num:=3 then it'll give 1 space, if we enter num:=4 then it'll give 2 spaces and so on.
########################################################################################

# :+ Use a plus sign to indicate if the result is positive or negative

message = f'The temperature is between {-1:+} and {+1:+} degrees celsius.'
print(message)

Output:
The temperature is between -1 and +1 degrees celsius.
########################################################################################

# :- Use a minus sign for negative values only

message = f'The temperature is between {-1:-} and {+1:-} degrees celsius.'
print(message)

Output:
The temperature is between -1 and 1 degrees celsius.
########################################################################################

# Use a space to insert an extra space before positive numbers (and a minus sign before negative numbers)


message = f'The temperature is between {-1: } and {2: } degrees celsius.'
print(message)

Output:
The temperature is between -1 and  2 degrees celsius.
########################################################################################

# :, Use a comma as a thousand separator

years = 13800000000
message = f'The universe is {years:,} years old.'
print(message)

Output:
The universe is 13,800,000,000 years old.
########################################################################################

# :_ Use a underscore as a thousand separator

years = 13800000000
message = f'The universe is {years:_} years old.'
print(message)

Output:
The universe is 13_800_000_000 years old.
########################################################################################

# :b Binary format

num = 5
message = f'The binary format of {num} is {num:b}.'
print(message)

Output:
The binary format of 5 is 101.
########################################################################################

# :d Decimal format

num = 0b101
message = f'The decimal value of {num} is {num:d}.'
print(message)

Outupt:
The decimal value of 5 is 5.
########################################################################################

# :o Octal format

num = 10
message = f'The octal format of {num} is {num:o}'
print(message)

Output:
The octal format of 10 is 12
########################################################################################

# :x Hex format, lower case

message = f'The hexa format of {255} is {255:x}'
print(message)

Output:
The hexa format of 255 is ff
########################################################################################

# :X Hex format, upper case

message = f'The hexa format of {255} is {255:X}'
print(message)

Output:
The hexa format of 255 is FF
########################################################################################

# :% Percentage format

num = 2
message = f'You scored {num:%}'
print(message)

Output:
You scored 200.000000%

num = 2
message = f'You scored {num:.0%}'
print(message)

Output: You scored 200%
########################################################################################

# :c Converts the value into the corresponding unicode character

num = 3
message = f'The unicode value of {num} is {num:c}.'
print(message)

Output:
The binary format of 3 is ♥.

# with each number there is a corresponding unicode attached. But not all numbers have it.
########################################################################################

# :e Scientific format, with a lower case e

message = f'We have {5:e} chickens.'
print(message)

Output:
We have 5.000000e+00 chickens.
########################################################################################

# :E Scientific format, with a upper case E

message = f'We have {11:E} chickens.'
print(message)

Output:
We have 1.100000E+01 chickens.
########################################################################################

# :f Fix point number format	|| #Use "f" to convert a number into a fixed point number, default with 6 decimals

num = 10
message = f'The price is {num:.2f} dollars today.'
print(message)

Output:
The price is $10.00 today.


num = 10
message = f'The price is ${num:f}.'
print(message)

Output:
The price is $10.000000.
########################################################################################

# :F Fix point number format, in uppercase format (show inf and nan as INF and NAN)

x = float('inf')
message = f'The price is {x:F}.'
print(message)

Output:
The price is INF.

x = float('INF')
message = f'The price is {x:f}.'
print(message)

Output:
The price is inf.
########################################################################################

