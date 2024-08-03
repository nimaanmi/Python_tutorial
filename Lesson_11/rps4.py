#
#

import sys
import random
from enum import Enum

game_count = 0


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

    def decide_winner(player, computer):
        if player == 1 and computer == 3:
            return '🎉 Player wins!'
        elif player == 2 and computer == 1:
            return '🎉 Player wins!'
        elif player == 3 and computer == 2:
            return '🎉 Player wins!'
        elif player == computer:
            return '😱 It\'s a draw!'
        else:
            return '🐍 Computer wins!'

    game_result = decide_winner(player, computer)
    print(game_result)
  
    global game_count
    game_count = game_count + 1

    print('\nGame count: ' + str(game_count))
    # The game_count outputs how many times we've played the game, and even though we run the function again and again it won't loose the count
    # because the count is not store inside the function, it's stored in the global scope outside of the function

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



