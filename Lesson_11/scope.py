SCOPE

There are different types of scopes.

1. Global scope
2. Local scope

# Local scope


def greeting(name):
    colour = 'blue'
    print(colour)
    print(name)				# here name is the parameter of the function 'greeting', it's not the global scope variable name.


greeting('John')

Output:
blue
John
---

# Global scope

name = 'Dave'


def greeting():
    colour = 'blue'
    print(colour)
    print(name)				# we are calling the global scope variable that is outside the function.


greeting()

Output:
blue
Dave
---

# It's not possible to call a local variable outside of that function anywhere else.

def greeting():
    colour = 'blue'
    print(colour)


greeting()
print(colour)				# it'll just not work, it'll come up with error during the code.

Output:
NameError: name 'colour' is not defined
---

# we can also call one function inside another function.

def greeting(name):
    colour = 'blue'
    print(colour)
    print(name)


greeting('John')


def another():
    greeting('Dave')


another()

Output:
blue
John
blue
Dave
---

# we can also define one function inside another function.

def another():
    colour = 'blue'

    def greeting(name):
        print(colour)
        print(name)

    greeting('Dave')


another()

Output:
blue
Dave

# Why do we need a funciton inside a funciton?
# It's helpful when we are workig on a team with other developers. 
# So, we try to keep the global scope as unpolluted or with as few things as possible and we try to put everything else inside of functions.
---

# we cannot call a child function outside of the parent function.

def another():
    colour = 'blue'

    def greeting(name):
        print(colour)
        print(name)

    greeting('John')


another()
greeting()

Output:
NameError: name 'greeting' is not defined
---

# what if we want to modify the assignment of a variable inside of a function but the variable was initially defined in the global scope?

count = 1


def another():
    count = 2
    print(count)


another()

Output:
2					# What it does here is it creates a new variable called count inside the function. It's not modifying the global variable.
---

Same way

count = 1


def another():
    count = count + 1			# what it does here is creates a local variable called 'count' but it doesn't have a value defined to it so it doesn't perform a task.
    print(count)


another()

Output:
UnboundLocalError: cannot access local variable 'count' where it is not associated with a value
---

# we can modify the global variable inside a function like this.
# if we want to modify a global variable inside a function, we'll have to use the global keyword before the variable name on one line, then modify it on the next line.


count = 1


def another():
    global count
    count = count + 1
    print(count)


another()

Output:
2
---

# we can also modify a variable inside a parent function from child function


def another():
    colour = 'blue'
    print(colour)

    def greeting():
        nonlocal colour			# nonlocal keyword tells our greeting function that it's going to be using colour from the parent function
        colour = 'red'
        print(colour)
    greeting()


another()

Output:
blue
red
---








