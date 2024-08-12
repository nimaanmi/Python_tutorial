#

import sys
import random
from enum import Enum

# we are putting a default value as playerone to the parameter name inside the main function rps(), just in case this will be used somewhere that it doesn't receive that name
# so we don't have an error if that happens.
# we are also adding personal touch like please and thank you, adding the argument name at places where player's name is needed, with the help of the argsparse module.

def rps(name='playerOne'):
    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_rps():
        nonlocal name
        nonlocal player_wins
        nonlocal python_wins

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSOR = 3

        playerchoice = input(
            f'{name}, please enter........\n1 for Rock\n2 for Paper\n3 for Scissor\n\n')
        if (playerchoice not in ['1', '2', '3']):
            print(f'{name}, please enter 1, 2, or 3')
            return play_rps()
        player = int(playerchoice)

        computerchoice = random.choice('123')
        computer = int(computerchoice)

        print(f'\n{name} entered: {
            str(RPS(player)).replace('RPS.', '').title()}')
        print(f'Python entered: {
            str(RPS(computer)).replace('RPS.', '').title()}')
        print()

        def decide_winner(player, computer):
            nonlocal name
            nonlocal player_wins
            nonlocal python_wins

            if player == 1 and computer == 3:
                player_wins = player_wins + 1
                return f'🎉 {name}, you win!'
            elif player == 2 and computer == 1:
                player_wins = player_wins + 1
                return f'🎉 {name}, you win!'
            elif player == 3 and computer == 2:
                player_wins = player_wins + 1
                return f'🎉 {name}, you win!'
            elif player == computer:
                return '😱 It\'s a draw!'
            else:
                python_wins = python_wins + 1
                return f'🐍 Python wins!\nSorry {name}...🥲'

        game_result = decide_winner(player, computer)
        print(game_result)

        nonlocal game_count
        game_count = game_count + 1

        print(f'Game count: {str(game_count)}')
        print(f'{name}\'s wins: {str(player_wins)}')
        print(f'Python wins: {str(python_wins)}')

        print(f'\nPlay again, {name}?')
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
            sys.exit('Bye {name}!👋')

    return play_rps


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
        description='Provides a personalized game experience.')
    parser.add_argument(
        '-n', '--name', metavar='name',
        required=True, help='The name of the person playing the game.'
    )
    args = parser.parse_args()

    rock_paper_scissor = rps(args.name)
    rock_paper_scissor()

#
# we cannot use the play button, like we used to use before
# we'll have to open the terminal and type in: py rps8.py -n 'Dave'

Dave, please enter........
1 for Rock
2 for Paper
3 for Scissor

3

Dave entered: Scissor
Python entered: Rock

🐍 Python wins!
Sorry Maan...🥲
Game count: 1
Dave's wins: 0
Python wins: 1

Play again, Dave?

Y for Yes
Q for Quit


