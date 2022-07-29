from ten_thousand.game_logic import GameLogic


def play(roller=GameLogic.roll_dice, num_rounds=20):
    """
    play Ten Thousand game

    Args:
        roller: optional dice rolling function. Default is GameLogic.roll_dice
        num_rounds: optional number of rounds. Default of 20

    Returns:
        None

    """
    chocie = invite_to_play()
    if chocie == 'y':
        start_game(num_rounds)
    else:
        decline_game()


def invite_to_play():
    """
    Display welcome message and prompt them to play or decline
    Returns:
        string "y" or "n"
    """
    print('Welcome to ten thousand game')
    print('(y)es to play or (n)o to decline')
    choice = input("> ")
    return choice


def start_game(num_rounds):
    """
    Start the game and run for given number of rounds
    Args:
        num_rounds:

    Returns:
        None
     """
    round_num = 1
    while round_num < 21:
    do_round(round_num)


def do_round(round_num):
    """
    Play a round of the game
    Args:
        round_num:

    Returns:
        integer for number of points scored in the round
        -1 has special meaning for "quit"
    """

    print(f'Starting round {round_num}')
    return 1


# def do_round(round_num):
#     """
#     Play a round of the game
#     Args:
#         round_num:
#
#     Returns:
#         integer for number of points scored in the round
#         -1 has special meaning for "quit"
#     """
#     pass


def zilch():
    """
    Display zilch message
    Returns:
        None
    """
    pass


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
    pass


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


def format_roll(roll):
    """
    converts given roll into display friendly string

    Args:
        roll: e.g. (5, 1, 1, 4, 5, 5)

    Returns:
        string: e.g. *** 5 1 1 4 5 5 ***
    """
    pass


def decline_game():
    """
    Displays message to declining player
    Returns:
        None
    """
    print('OK. Maybe another time')


if __name__ == '__main__':
    play()
