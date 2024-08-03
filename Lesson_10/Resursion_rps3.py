# return can only be used within a function.

import sys
import random
from enum import Enum


def play_rps():
    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSOR = 3

    playerchoice = input(
        '\nEnter........\n1 for Rock\n2 for Paper \n3 for Scissor\n\n')
    if (playerchoice not in ['1', '2', '3']):
        print('You need to enter 1, 2, or 3')
        return play_rps()
    player = int(playerchoice)

    computerchoice = random.choice('123')
    computer = int(computerchoice)

    print()
    print('\nPlayer entered: ' + str(RPS(player)).replace('RPS.', ''))
    print('Computer entered: ' + str(RPS(computer)).replace('RPS.', ''))
    print()

    if player == 1 and computer == 3:
        print('🎉 Player wins!')
    elif player == 2 and computer == 1:
        print('🎉 Player wins!')
    elif player == 3 and computer == 2:
        print('🎉 Player wins!')
    elif player == computer:
        print('😱 It\'s a draw!')
    else:
        print('🐍 Python wins!')

    print('\nPlay again?')

    while True:
        play_again = input('\nY for Yes\nQ for Quit\n')
        if (play_again.lower() not in ['y', 'q']):
            continue
        else:
            break

    if (play_again.lower() == 'y'):
        return play_rps()
    else:
        print('🎉🎉🎉')
        print('Thank you for playing!')
        sys.exit('Bye! 👋')


play_rps()
