from random import randint
from collections import Counter
from ten_thousand.banker import Banker
from ten_thousand.game_logic import GameLogic

'''
Game class to handle: 
start game, start round, roll dice, bank score, 
end round, calculate points, end game
'''

# def play_game():
#     choice = invite_play()
#     if choice == 'y':
#         start_game()
#     else:
#         decline_game()

bank = Banker()
zilch = False


def play_game():
    """
       Display welcome message and prompt them to play or decline the game
       Returns:
           no returns, init the start or decline game function
       """
    print('Welcome to Ten Thousand')
    print('(y)es to play or (n)o to decline')
    choice = input("> ")
    if choice == 'y':
        start_game()
    else:
        decline_game()


def start_game(num_rounds):
    """
    Start the game and run for given number of rounds
    Args:
        num_rounds:

    Returns:
        None
    """
    round_num = 1
    total_points = 0
    while round_num <= 10:
        round_result = start_round(round_num, roll_dice)
        if round_result == 'q':
            break
        total_points += round_result
        round_num += 1
        end_game_msg(total_points)


def end_game_msg(total_points):
    print(f"Thanks for playing. You earned {total_points} points")


def start_round(round_num, roll_dice):
    round_points = 0
    print(f'Starting round {round_num}')
    print('Rolling 6 dice...')
    display_numbers()
    print("Enter dice to keep, or (q)uit:")
    keep_or_quit = input("> ")
    dice_roll_list = Counter(roll_dice)
    if keep_or_quit == 'q':
        end_game_msg()
    else:
        dice_keep_list = [int(i) for i in keep_or_quit]
    unbanked_points = GameLogic.calculate_score(dice_keep_list)


bank_roll_quit()
choice = bank_roll_quit(unbanked_points, num_dice)
#
#     if choice == 'q':
#         return 'q'
#     elif choice == 'b':
#         return unbanked_points
#     elif choice == 'r':
#         continue


round_points += sub_result
print(f"You banked {round_points} in round {round_num}")
return round_points


def display_numbers():
    roll = roller(dice_num)
    formatted_roller = " ".join([str(i) for i in roller])
    print(f"*** {formatted_roller} ***")

# def confirm_keepers(roll):
#     pass
#
#
# def sub_round(roll_dice):
#     num_dice = 6
#     unbanked_points = 0
#
#     while True:
#         roll = do_roll(num_dice, roll_dice)
#         display_roll(roll)
#
#         if zilch(roll)
#             return 0
#
#         keepers = confirm_keepers(roll)
#         if keepers == 'q':
#             return 'q'

# unbanked_points += GameLogic.calculate_score(keepers)
# num_dice -= len(keepers)
# if num_dice == 0:
#     num_dice = 6 #  reset to six
# bank_roll_quit()


def zilch():
    """
    Display zilch message
    Returns:
        None
    """
    if GameLogic.calculate_score(roll_dices) == 0
        bank.clear_shelf()
        print('Zilch! round over.')
        round_total = 0
        handle_bank()
        zilch = True


def handle_bank(self):
    print(f"You banked {round_total} points in round {round_num}")
    bank.shelf(round_total)
    bank.bank()
    game_total += round_total
    print(f"Total score is {bank.balance} points")
    round_total = 0


def confirm_keepers(roll):
    """
    Return values that user would like to keep after being validated
    Loops until user quits or follows the rules (aka keeps values that are valid)
    Args:
        roll: tuple of integers
    Returns:
        tuple of values to keep aka "keepers"
        empty tuple signals a "quit"
    """
    if GameLogic.validate_keepers(roll, user_kept):
        round_total += GameLogic.calculate_score(user_kept)
        dice_num = dice_num - len(user_kept)
        return user_kept
    else:
        print("Cheater!!! Or possibly made a typo...")
        print(f"*** {roll_string} ***")
        get_dice_to_keep()


def convert_keepers(keeper_string):
    """
    converts a given string of dice values to keep into a tuple of integers
    Args:
        keeper_string:

    Returns:
        tuple of integers

    """
    pass


def do_roll(num_dice):
    """
    Display to user a new roll of given number of dice in formatted form
    Args:
        num_dice:

    Returns:
        return the roll (tuple of integers

    """
    pass



def bank_roll_quit(unbanked_points, left_dice):
    print(f"You have {unbanked_points} unbanked points and {left_dice} dice remaining)
    print("(r)oll again, (b)ank your points or (q)uit:")


def roll_dices(self, roller):
    print(f"Rolling {self.dice_remaining} dice...")


def decline_game():
    print('OK. Maybe another time')


if __name__ == "__main__":
    play_game()
