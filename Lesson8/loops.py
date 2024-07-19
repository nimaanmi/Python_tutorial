Loops

There are 2 types of loops in python.
While loop
For   loop

While loop: 
A while loop will execute a block of code while a condition is true.

For this, we have to set a value first.		Ex: value = 1
Then use the while loop condition		Ex: while value < 10:
Next line, here we have a block of code inside the while loop	Ex: print(value)
# now we must increment the value to go ahead and make it greater than 10 at some point.
# Or if not atleast equal to 10, the way we have this current loop set becuase, if not we'll have an endless loop or an infinite loop
# that could crash out computer and it would use up all the memory and it would just go on forever and we don't want that to happen.
So, we increment the value			Ex: value += 1
This is going to increment every time it goes through the loop and it will eventually be equal to 10 or greater and the loop will stop.
Save and run.

value = 1
while value <= 10:
    print(value)
    value += 1

Output:
1
2
3
4
5
6
7
8
9				# it goes 9 times through the loop and exexutes each time and exits when the value reaches 10 as per the while condition.
			

# break 
# we can also stop a loop in another way besides making the condition true by using a break statement.
value = 1
while value <= 10:
    print(value)
    if value == 5:
        break			# here it breaks out of the loop if the value == 5
    value += 1

Output:
1
2
3
4
5

# continue
value = 1
while value <= 10:
    value += 1
    if value == 5:
        continue		if we want to skip a value (in this case 5) we have to have increment first, then a condition and then the print
    print(value)

Output:
2
3
4
6
7
8
9
10
11

# else to a while loop

else in a while loop will only execute if the while loop actually completes as it should (if we use a break statement, it'll not execute the else statement)
So, if a while loop is no longer true then the else will occur.

value = 1
while value <= 10:
    value += 1
    if value == 5:
        continue
    print(value)
else:
    print('Value is now equal to ' + str(value))			# we are type casting the object 'value' as by default it's an interger and we cannot concatenate int.

Output:
2
3
4
6
7
8
9
10
11
Value is now equal to 11
===
===
===

For loop

iterate = repetitive execution of the same block of code over and over.
A for loop repeatedly executes over a sequence of collection data types or individual characters of a string as long as the condition is satisfied.
A for loop iterates over a sequence and the sequence can be contents of a collection data type like lists, tuples, dictionaries or sets, or it can even be the individual characters of a string

names = ['Dave', 'Sara', 'John']
for x in names:
    print(x)

Output: 
Dave
Sara
John

for x in 'Mississippi':

'x' represents each value in the list as it repeatedly executes through the for loop.
'x' represents each value in the list as it iterates through the for loop.
In place of x we can use any other word we want like 'name in names'.

names = ['Dave', 'Sara', 'John']
for x in names:
    if x == 'Sara':
        break
    print(x)

Output:
Dave

names = ['Dave', 'Sara', 'John']
for x in names:
    if x == 'Sara':
        continue
    print(x)

Output:
Dave
John

# Ranges
# We can have for loop that iterates through a range 

for x in range(4):
    print(x)

Output:
0
1
2
3

# Just like an index in a list, a range starts from 0.

for x in range(2, 4):
    print(x)

Output:
2
3

# It's going to start with the number that we include if we specify a start point but it's not going to end with the number that we include as range starts from 0.

# we can also specify range how to increment, in place of the default increment by 1 each time, we could increment by 5 or any other value.

for x in range(0, 50, 5):
    print(x)

Output:
0
5
10
15
20
25
30
35
40
45
50
55
60
65
70
75
80
85
90
95

# else statement with a for loop.
for x in range(5, 51, 5):
    print(x)
else:
    print('Glad that\'s over!')

Output:
5
10
15
20
25
30
35
40
45
50
Glad that's over!

# Nested loops

# we are using first list in outer loop, 2nd list in inner loop
names = ['Dave', 'Sara', 'John']
actions = ['codes', 'eats', 'sleeps']

for name in names:
    for action in actions:
        print(name + ' ' + action + '.')

Output:
Dave codes.
Dave eats.
Dave sleeps.
Sara codes.
Sara eats.
Sara sleeps.
John codes.
John eats.
John sleeps.

Here, name in names presents each value in the list as it iterates through the for loop.
How it works:
we are giving each index a name as namex
So, name1 = Dave, name2 = Sara, name3 = John, and so on
Same with action in actions.
So, action1 = Codes, action2 = eats, action3 = sleeps
So, we run the outerloop first which is name in names, the we run the innerloop which action in actions
So, it executes like
name1 + action1		# because we are adding those two list items in the print function.
name1 + action2
name1 + action3
	now it continues to the next index in first loop called names.
name2 + action1
name2 + action2
name2 + action3
	now it continues to the next index in first loop called names.
name3 + action1
name3 + action2
name3 + action3
And so on...

# we are using 2nd list in outer loop, and 1st loop in innter loop.

names = ['Dave', 'Sara', 'John']
actions = ['codes', 'eats', 'sleeps']

for action in actions:
    for name in names:
        print(action + ' ' + name + '.')			# we have interchanged the print items objects

Output:
codes Dave.
codes Sara.
codes John.
eats Dave.
eats Sara.
eats John.
sleeps Dave.
sleeps Sara.
sleeps John.

# the same above example but interaching the print items objects
names = ['Dave', 'Sara', 'John']
actions = ['codes', 'eats', 'sleeps']

for action in actions:
    for name in names:
        print(name + ' ' + action + '.')

Output:
Dave codes.
Sara codes.
John codes.
Dave eats.
Sara eats.
John eats.
Dave sleeps.
Sara sleeps.
John sleeps.


---
# Nested for loop examples: https://www.youtube.com/watch?v=fX64q6sYom0
---

# we always start the print from the left.
# It's printed row by row [row are horizontal]. And we cannot go back to the previous row, we have to complete and move forward.
1. Size [How many rows you want in the pattern?]
		n = int(input('Number of rows: '))		# we can ask user to input or
		def pattern(n):					# function parameter or
		n = 5						# if we have the size in the question.
2. Putting together nested loops
3. 
4. print statement


n = 5
for j in range(n):
    print('*')

Output:
*
*
*
*
*

#We see that the output is line by line. But we want to have it one line.

n = 5
for j in range(n):
    print('*', end='')

Output:
*****

# we want to print a square using the stars.

n = 5
for i in range(n):
    for j in range(n):
        print('*', end=' ')				# end='' is used to print STARS in the same line
    print()						# print() is used to go to next line after each outer loop.

Output:
* * * * * 
* * * * *
* * * * *
* * * * *
* * * * *

Here, i values are in the outer loop (row=horizontal) and j values are in the inner loop(column=vertical).
i starts with 0, then it goes to inner loop where j starts with 0 and it increments each value 1, 2, 3, 4 and stops at 4 and breaks the loop and goes back to the outer loop.
The outer loop now increments to 1(goes to the 2nd row), and goes to the inner loop where it starts from 0 again and increments each value till 4 and breaks the loop.


Q. Increasing triangle Pattern

n = 5
for i in range(n):
    for j in range(i+1):
        print('*', end=' ')
    print()

Output:
* 
* *
* * *
* * * *
* * * * *

Q. Decreasing triangle Pattern

n = 5
for i in range(n):
    for j in range(i, n):
        print('*', end=' ')
    print()

Output:
* * * * * 
* * * *
* * *
* *
*

Q Creating a right sided triangle.
It has 2 triangles. 1st is decreasing space triangle. 2nd is increasing star triangle

n = 5
for i in range(n):
    for j in range(i, n):
        print(' ', end=' ')
    for j in range(i+1):
        print('*', end=' ')
    print()

Output:
          * 
        * *
      * * *
    * * * *
  * * * * *

Q. Creating a right sided triangle.
It has 2 triangles. 1st increasing triangle of space, 2nd decreasing triangle of stars

n = 5
for i in range(n):
    for j in range(i+1):
        print(' ', end=' ')
    for j in range(i, n):
        print('*', end=' ')
    print()

Output:
  * * * * * 
    * * * *
      * * *
        * *
          *

Q. Creating a hill pattern
It has 3 triangles. 1st decreasing spaces, 2nd increasing stars, 3rd increasing stars.

n = 5
for i in range(n):
    for j in range(i, n):
        print(' ', end=' ')
    for j in range(i+1):
        print('*', end=' ')
    for j in range(i):
        print('*', end=' ')
    print()

Output:
          * 
        * * *
      * * * * *
    * * * * * * *
  * * * * * * * * *

Q. Creating a reverse hill pattern
It has 3 triangles. 1st increasing spaces, 2nd decreasing stars, 3rd decreasing stars

n = 5
for i in range(n):
    for j in range(i+1):
        print(' ', end=' ')
    for j in range(i, n):
        print('*', end=' ')
    for j in range(i, n-1):
        print('*', end=' ')
    print()

Output:
  * * * * * * * * * 
    * * * * * * *
      * * * * *
        * * *
          *

Q. Diamond patten
n = 5
for i in range(n-1):
    for j in range(i, n):
        print(' ', end=' ')
    for j in range(i+1):
        print('*', end=' ')
    for j in range(i):
        print('*', end=' ')
    print()
for i in range(n):
    for j in range(i+1):
        print(' ', end=' ')
    for j in range(i, n):
        print('*', end=' ')
    for j in range(i, n-1):
        print('*', end=' ')
    print()

Output:
          * 
        * * *
      * * * * *
    * * * * * * *
  * * * * * * * * *
    * * * * * * *
      * * * * *
        * * *
          *


Q. Pyramid pattern

n = 5
for i in range(n):
    for j in range(i, n):
        print(' ', end='')
    for j in range(i+1):
        print('*', end=' ')
    print()

Output:
     * 
    * *
   * * *
  * * * *
 * * * * *

---
---
---











---

# Nested for loop examples:

# print a right triangle using nest for loop
row = 7
for i in range(1, row+1):
    for j in range(1, i+1):
        print('*', end=' ')
    print(' ')

Output:
*  
* *
* * *
* * * *
* * * * *
* * * * * *
* * * * * * *


list_fruits = ['Mango', 'Apple', 'Grapes', 'Banana']
for fruit in list_fruits:
    for i in fruit:
        print(i, end='*')
    print()

Output:
M*a*n*g*o*
A*p*p*l*e*
G*r*a*p*e*s*
B*a*n*a*n*a*

# print values of items in two lists 
colour = ['red', 'green', 'blue']
items = ['apple', 'veggies', 'shirt']
for x in colour:
    for y in items:
        print(x, y)
        print('')

Output:
red apple

red veggies

red shirt

green apple

green veggies

green shirt

blue apple

blue veggies

blue shirt

# print right triangle using for loop
for i in range(11):
    for j in range(i):
        print('*', end=' ')
    print('')

Output:
*
* *
* * *
* * * *
* * * * *
* * * * * *
* * * * * * *
* * * * * * * *
* * * * * * * * *
* * * * * * * * * *

# print right triangle using while loop
i = 11
while i > 0:
    j = 11
    while j > i:
        print('*', end=' ')
        j -= 1
    i -= 1
    print()

Output:
*
* *
* * *
* * * *
* * * * *
* * * * * *
* * * * * * *
* * * * * * * *
* * * * * * * * *
* * * * * * * * * *

# how to append two lists
list1 = [10, 25, 30]
list2 = [60, 15, 50]
result = []
for i in list1:
    for j in list2:
        result.append(i+j)
print(result)

Output:
[70, 25, 60, 85, 40, 75, 90, 45, 80]

# multipying two lists:
list1 = [2, 4, 6]
list2 = [2, 4, 6]
for i in list1:
    for j in list2:
        print(i, '*', j, '=', i*j)

Output:
2 * 2 = 4
2 * 4 = 8
2 * 6 = 12
4 * 2 = 8
4 * 4 = 16
4 * 6 = 24
6 * 2 = 12
6 * 4 = 24
6 * 6 = 36

# multiplying two lists, excluding if same i == j.
list1 = [2, 4, 6]
list2 = [2, 4, 6]
for i in list1:
    for j in list2:
        if i == j:
            continue
        print(i, '*', j, '=', i*j)

Output:
2 * 4 = 8
2 * 6 = 12
4 * 2 = 8
4 * 6 = 24
6 * 2 = 12
6 * 4 = 24

# print perfect numbers between 1 and 100
a = 1
while a <= 100:
    y_sum = 0

    for i in range(1, a):
        if a % i == 0:
            y_sum += i
    if y_sum == a:
        print('Perfect number: ', a)
    a += 1

Output:
Perfect number:  6
Perfect number:  28

# print each elements 5 times
fruits = ['apple', 'orange', 'kiwi']
for fruit in fruits:
    count = 0
    while count < 6:
        print(fruit, end=' ')
        count += 1
    print()

Outut:
apple apple apple apple apple apple 
orange orange orange orange orange orange
kiwi kiwi kiwi kiwi kiwi kiwi


Examples of while loop:

1. print something 5 times

i = 1
while i <= 5:
    print('Focus')
    i = i + 1

Output:
Focus
Focus
Focus
Focus
Focus

2. 

i = 1
while i <= 4:
    print('Mango', end=' ')
    j = 1
    while j <= 4:
        print('Rocks', end=' ')
        j = j + 1
    i = i + 1
    print()

Output:
Mango Rocks Rocks Rocks Rocks 
Mango Rocks Rocks Rocks Rocks 
Mango Rocks Rocks Rocks Rocks 
Mango Rocks Rocks Rocks Rocks 

3. Creating a square using stars

i = 1
while i <= 4:
    j = 1
    while j <= 4:
        print('*', end=' ')
        j = j + 1
    i = i + 1
    print()

Output:
* * * * 
* * * *
* * * *
* * * *

4. Print numbers from 1-100 skipping the numbers divisible by 3 & 5

i = 1
while i <= 100:
    j = i % 3
    k = i % 5
    if (j != 0 and k != 0):
        print(i)
    i = i + 1

Output:
1
2
4
7
8
11
13
14
16
17
19
22
23
26
28
29
31
32
34
37
38
41
43
44
46
47
49
52
53
56
58
59
61
62
64
67
68
71
73
74
76
77
79
82
83
86
88
89
91
92
94
97
98

5. Calculate the sum of numbers until user enters 0

number = int(input('Enter a number: '))

total = 0
while number != 0:
    total = total + number
    number = int(input('Enter a number: '))
print('The sum is: ', total)

Output: 
Enter a number: 4
Enter a number: 7
Enter a number: 9
Enter a number: 0
The sum is:  20

6. 

s = 'tomatolala'
count = 0
while count < len(s):
    print(s[count])
    count = count + 1

Output:
t
o
m
a
t
o
l
a
l
a

7. Print Fibonacci numbers from 1 to 10

a = 0						# variable a is assigned 0
b = 1						# variable b is assigned 1
n = 3						# counter n = 3
while n <= 10:
    total = a + b				# We are adding a and b and saving it in variable total.
    a = b					# we are re-assigning the value of variable a with b
    b = total					# we are re-assigning the value of variable of b with total
    print(total)				# we are printing total from above.
    n = n + 1					# we are incrementing the counter n with 1 number each time till it comes out of the loop i.e., when it becomes more than 10.

Output:
1
2
3
5
8
13
21
34

