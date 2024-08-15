Closures

# Closure is a function having access to the scope of its parent function after the parent function has returned.
# Instead of returning any value we are going to return the child function.
# Notice we are not calling the child function into action by putting the parentheses after it.
# We are just returning this nested child function when we call the parent function.


def parent_function(person):
    coins = 3

    def play_game():
        nonlocal coins
        coins = coins - 1

        if coins > 1:
            print('\n' + person + ' has ' + str(coins) + ' coins left.')
        elif coins == 1:
            print('\n' + person + ' has ' + str(coins) + ' coin left.')
        else:
            print('\n' + person + ' is out of coins.')

    return play_game


tommy = parent_function('Tommy')
jenny = parent_function('Jenny')

tommy()         # Now we call tommy() as tommy is a function now.
tommy()
jenny()

Output:
Tommy has 2 coins left.

Tommy has 1 coin left.

Jenny has 2 coins left.
########################################################################################

# The scope can also be as a parameter inside the parentheses of the parent function.
# Creating a nested function and using closure accessing a value from the parent function is one good way to avoid creating global variables.
### But when you need to access a variable from a parent still on this just creates another level.

def parent_function(person, coins):

    def play_game():
        nonlocal coins
        coins = coins - 1

        if coins > 1:
            print('\n' + person + ' has ' + str(coins) + ' coins left.')
        elif coins == 1:
            print('\n' + person + ' has ' + str(coins) + ' coin left.')
        else:
            print('\n' + person + ' is out of coins.')

    return play_game


tommy = parent_function('Tommy', 3)
jenny = parent_function('Jenny', 5)

tommy()         # Now we call tommy() as tommy is a function now.
tommy()
jenny()
tommy()

Output:
Tommy has 2 coins left.

Tommy has 1 coin left.

Jenny has 4 coins left.

Tommy is out of coins.
########################################################################################

# Indepth understading of closure

# 1. Basic Nested Function with Immediate Execution
    
def outer_scope():
    name = 'Sam'
    city = 'New York'

    def inner_scope():
        print(f"Hello {name}, Greetings from {city}")

    return inner_scope()
    
outer_scope()

Output: 
"Hello Sam, Greetings from New York".

# In this example, the outer_scope function defines two local variables: name and city.
# It then defines and immediately calls inner_scope, which prints a greeting message using the name and city variables from the enclosing scope.
# When outer_scope is called, the nested function inner_scope runs, producing the greeting message: "Hello Sam, Greetings from New York".
########################################################################################
    
# 2. Returning the Inner Function
# Now, let's modify the example to return the inner function without executing it immediately:

def outer_scope():
    name = 'Sam'
    city = 'New York'

    def inner_scope():
        print(f"Hello {name}, Greetings from {city}")

    return inner_scope
    
# Assigning the inner function to a variable
greeting_func = outer_scope()

# Calling the inner function
greeting_func()

Output:
"Hello Sam, Greetings from New York".

# Here, outer_scope defines name and city as variables similarly to the above example.
# It then defines and returns the inner_scope function but this time without calling it (that is, inner_scope instead of inner_scope()),
# When greeting_func = outer_scope() is executed, it assigns the inner_scope function returned by outer_scope to greeting_func.
# Now, greeting_func holds a reference to the inner_scope function. Calling greeting_func() executes inner_scope, which prints: "Hello Sam, Greetings from New York".
# Even though outer_scope has finished executing by the time we call greeting_func(), the inner_scope function (now referenced by greeting_func) retains access to the variables name and city from its enclosing scope.
# This is what makes it a closure – it "closes over" the variables from its containing scope.
########################################################################################

# Maintaining State in GUI Applications
# In Python, closures can be used to maintain state in graphical user interface (GUI) applications, such as those created with Tkinter [https://github.com/samyuii/Tkinter-V3].

import tkinter as tk

def create_counter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        print(f'Button clicked {count} times')
    return counter

root = tk.Tk()
root.title('Counter Example')

counter = create_counter()
button = tk.Button(root, text='Click me', command=counter)
button.pack(pady=20)

root.mainloop()

Explanation:
1. create_counter is a higher-order function that initializes count to 0 and defines a nested counter function.
2. The counter function is a closure that captures the count variable from the enclosing scope.
3. The nonlocal keyword allows the closure to modify the count variable.
4. Each time the button is clicked, the counter function is invoked, and it increments and prints the count.

########################################################################################


