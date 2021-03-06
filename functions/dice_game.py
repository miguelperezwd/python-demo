# This program will allow 2 users to play a dice rolling game

import random

def roll_dice():
    dice_total = random.randint(1,6) + random.randint(1,6)
    return dice_total

def main():
    player1 = input("Enter player 1's name: ")
    player2 = input("Enter player 2's name: ")

    # Roll the dice for both players using the function
    roll1 = roll_dice()
    roll2 = roll_dice()

    # Show the results
    print(player1, 'rolled', roll1)
    print(player2, 'rolled', roll2)

    # Determine the winner
    if roll1 > roll2:
        print(player1, 'wins!')
    elif roll2 > roll1:
        print(player2, 'wins!')
    else:
        print('You tie!')

main()