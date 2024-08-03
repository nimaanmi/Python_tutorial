
# improving the RPS / Rock Paper Scissor game so we don't have to start it over and over again.

import sys
import random
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSOR = 3


playagain = True
while playagain:

    playerchoice = input(
        'Enter.......\n1 for Rock\n2 for Paper\n3 for Scissor\n\n')
    player = int(playerchoice)

    if player < 1 or player > 3:
        sys.exit('You need to enter 1, 2, or 3')

    computerchoice = random.choice('123')
    computer = int(computerchoice)

    print()
    print('\nPlayer entered: ' + str(RPS(player)).replace('RPS.', '').title())
    print('Python entered: ' + str(RPS(computer)).replace('RPS.', '').title())
    print()

    if player == 1 and computer == 3:
        print('🎉Player wins!')
    elif player == 2 and computer == 1:
        print('🎉Player wins!')
    elif player == 3 and computer == 2:
        print('🎉Player wins!')
    elif player == computer:
        print('😱It\'s a draw!')
    else:
        print('🐍 Python wins!')

    playagain = input('Play again? /nY for Yes\nQ for Quit\n\n')
    if playagain.lower() == 'y':
        continue
    else:
        print('🎉🎉🎉')
        print('Thank your for playing!')
        playagain = False

sys.exit('Bye! 👋')
