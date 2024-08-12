#

import sys
import random


def guess_number(name='playerOne'):
    game_count = 0
    player_wins = 0

    def play_guess_number():
        nonlocal name
        nonlocal player_wins

        playerchoice = input(
            f'{name}, guess which number I\'m thinking of... 1, 2, or 3\n\n')
        if (playerchoice not in ['1', '2', '3']):
            print(f'{name}, please enter 1, 2, or 3')
            return play_guess_number()
        player = int(playerchoice)

        computerchoice = random.choice('123')
        computer = int(computerchoice)

        print(f'\n{name}, you chose {str(player)}')
        print(f'I was thinking about the number {str(computer)}')
        print()

        def decide_winner(player, computer):
            nonlocal name
            nonlocal player_wins

            if player == computer:
                player_wins = player_wins + 1
                return f'🎉 {name}, you win!'
            else:
                return f'Sorry, {name}. Better luck next time. 🥲'

        game_result = decide_winner(player, computer)
        print(game_result)

        nonlocal game_count
        game_count = game_count + 1

        print(f'\nGame count: {str(game_count)}')
        print(f'\n{name}\'s wins: {str(player_wins)}')
        print(f'\nYour winning percentage: {(player_wins/game_count):.2%}')

        print(f'\nPlay again, {name}?')
        while True:
            play_again = input('\nY for Yes\nQ for Quit\n')
            if (play_again.lower() not in ['y', 'q']):
                continue
            else:
                break

        if (play_again.lower() == 'y'):
            return play_guess_number()
        else:
            print('🎉🎉🎉')
            print('Thank you for playing!')
            if __name__ == '__main__':
                sys.exit('Bye {name}!👋')
                # we are calling the guess_my_number() function directly from this file.
            else:
                # if not, if it's called from the arcade we say else: and return (have an empty return)
                # so we go back working with the code in the arcade file.
                return

    return play_guess_number


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
        description='Provides a personalized game experience.')
    parser.add_argument(
        '-n', '--name', metavar='name',
        required=True, help='The name of the person playing the game.'
    )
    args = parser.parse_args()

    guess_my_number = guess_number(args.name)
    guess_my_number()
