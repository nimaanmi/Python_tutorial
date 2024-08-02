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
---

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
---
