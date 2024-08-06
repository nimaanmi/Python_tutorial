

# we are using f-strings in this code, nothing else.
import sys
import random
from enum import Enum


def rps():
    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_rps():
        nonlocal player_wins
        nonlocal python_wins

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSOR = 3

        playerchoice = input(
            'Enter........\n1 for Rock\n2 for Paper\n3 for Scissor\n\n')
        if (playerchoice not in ['1', '2', '3']):
            print('You need to enter 1, 2, oe 3')
            return play_rps()
        player = int(playerchoice)

        computerchoice = random.choice('123')
        computer = int(computerchoice)

        print()
        print(
            f'Player entered: {str(RPS(player)).replace('RPS.', '').title()}'
        )
        print(
            f'Python entered: {str(RPS(computer)).replace('RPS.', '').title()}'
        )
        print()

        def decide_winner(player, computer):
            nonlocal player_wins
            nonlocal python_wins

            if player == 1 and computer == 3:
                player_wins = player_wins + 1
                return '🎉 Player wins!'
            elif player == 2 and computer == 1:
                player_wins = player_wins + 1
                return '🎉 Player wins!'
            elif player == 3 and computer == 2:
                player_wins = player_wins + 1
                return '🎉 Player wins!'
            elif player == computer:
                return '😱 It\'s a draw!'
            else:
                python_wins = python_wins + 1
                return '🐍 Python wins!'

        game_result = decide_winner(player, computer)
        print('\nGame result: ' + str(game_result))

        nonlocal game_count
        game_count = game_count + 1
        print(f'\nGame count: {str(game_count)}')
        print(f'player wins: {(player_wins)}')
        print(f'Python wins: {str(python_wins)}')

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
    return play_rps


play = rps()
play()
