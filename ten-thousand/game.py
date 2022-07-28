from random import randint
from collections import Counter


def play():
    choice = invite_play()
    if choice == 'y':
        start_game()
    else:
        decline_game()


def invite_play():
    print('Welcome to Ten Thousand')
    print('(y)es to play or (n)o to decline')
    choice = input("> ")
    return choice


def start_game():
    round_num = 1
    total_points = 0
    while round_num <= 10:
        round_result = this_round(round_num, roll_dice)
        if round_result == 'q':
            break
        total_points += round_result
        round_num += 1
        end_game(total_points)


def end_game_msg(total_points):
    print(f"Thanks for playing. You earned {total_points} points")


def this_round(round_num, roll_dice):
    round_points = 0
    print(f'Starting round {round_num}')
    print('Rolling 6 dice...')
    formatted_roller = " ".join([str(i) for i in roller])
    print(f"*** {formatted_roller} ***")

    sub_result = sub_round(roll_dice)
    if sub_result == 'q':
        return 'q'

    round_points += sub_result
    print(f"You banked {round_points} in round {round_num}")
    return round_points


def confirm_keepers(roll):
    pass


def sub_round(roll_dice):
    num_dice = 6
    unbanked_points = 0

    while True:
        roll = do_roll(num_dice, roll_dice)
        display_roll(roll)

        if zilch(roll)
            return 0

        keepers = confirm_keepers(roll)
        if keepers == 'q':
            return 'q'

        unbanked_points += GameLogic.calculate_score(keepers)
        num_dice -= len(keepers)
        if num_dice == 0:
            num_dice = 6

            choice = bank_roll_quit(unbanked_points, num_dice)

            if choice == 'q':
                return 'q'
            elif choice == 'b':
                return unbanked_points
            elif choice == 'r':
                continue


def do_roll():
    pass


def bank_roll_quit(unbanked_points, left_dice):
    print(f"You have {unbanked_points} unbanked points and {left_dice} dice remaining)
    print("(r)oll again, (b)ank your points or (q)uit:")


def roll_dices(self, roller):
    print(f"Rolling {self.dice_remaining} dice...")


def decline_game():
    print('OK. Maybe another time')


if __name__ == "__main__":
    play()
