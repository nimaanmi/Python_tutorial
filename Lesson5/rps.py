Creating a Rock Paper Scissor game

import sys                          # this is needed to exist the statement
import random                       # this is under to check random numbers.

print('')
playerchoice = input('Enter........\n1 for Rock\n2 for Paper\n3 for Scissor\n\n')       # keep cursor at the line end and press alt+z to wrap it properly.
player = int(playerchoice)

if player < 1 or player > 3:
    sys.exit('You need enter 1, 2, or 3')                                               # We need to learn how to exit the program.

computerchoice = random.choice('123')
computer = int(computerchoice)
print('')
print('You chose ' + playerchoice)
print('Python chose ' + computerchoice)
print('')

if player == 1 and computer == 3:
    print('You win')
elif player == 2 and computer == 1:
    print('You win')
elif player == 3 and computer == 2:
    print('You win')
elif player == computer:
    print('It\'s a draw')
else:
    print('Python wins')


Output:
Enter........
1 for Rock
2 for Paper
3 for Scissor

3
You chose 3
Computer chose 2

You win

##########################################################################################################

Let's improvise the above code.

import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSOR = 3

print('')
playerchoice = input('Enter........\n1 for Rock\n2 for Paper\n3 for Scissor\n\n')
player = int(playerchoice)

if player < 1 or player > 3:
    sys.exit('You need enter 1, 2, or 3')

computerchoice = random.choice('123')
computer = int(computerchoice)
print('')
print('You chose ' + str(RPS(player)))
print('Computer chose ' + str(RPS(computer)))
print('')

if player == 1 and computer == 3:
    print('You win')
elif player == 2 and computer == 1:
    print('You win')
elif player == 3 and computer == 2:
    print('You win')
elif player == computer:
    print('It\'s a draw')
else:
    print('Computer wins')


Output:
Enter........
1 for Rock
2 for Paper
3 for Scissor

3

You chose RPS.SCISSOR
Computer chose RPS.ROCK

Computer wins
##########################################################################################################

Let's improvise a bit more
Lets remove the "RPS." from the output
Also, let's add emojis        # windows+. will open emojis tab


import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSOR = 3

print('')
playerchoice = input('Enter........\n1 for Rock\n2 for Paper\n3 for Scissor\n\n')
player = int(playerchoice)

if player < 1 or player > 3:
    sys.exit('You need enter 1, 2, or 3')

computerchoice = random.choice('123')
computer = int(computerchoice)
print('')
print('You chose ' + str(RPS(player)).replace('RPS.', ''))
print('Computer chose ' + str(RPS(computer)).replace('RPS.', ''))
print('')

if player == 1 and computer == 3:
    print('🎉You win')
elif player == 2 and computer == 1:
    print('🎉You win')
elif player == 3 and computer == 2:
    print('🎉You win')
elif player == computer:
    print('😱It\'s a draw')
else:
    print('🐍Computer wins')


Output:
Enter........
1 for Rock
2 for Paper
3 for Scissor

1

You chose ROCK
Computer chose PAPER




