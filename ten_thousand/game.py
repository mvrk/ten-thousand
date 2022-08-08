from collections import Counter
from ten_thousand.banker import Banker
from ten_thousand.game_logic import GameLogic
import sys

'''
Game class to handle: 
start game, start round, roll dice, bank score, 
end round, calculate points, end game
'''


def zilch():
    print("****************************************")
    print("**        Zilch!!! Round over         **")
    print("****************************************")


def display_roll(dice_list):  # transfer list[1,1,1,2,2,2] to *** 1 1 1 2 2 2 ***
    roll_string = ' '.join(map(str, dice_list))
    return roll_string


def validate_keepers(dice_list, user_kept):
    dice_list = Counter(dice_list).most_common()
    user_kept = Counter(user_kept).most_common()
    for i in range(len(dice_list) - 1):
        if user_kept[i][1] > dice_list[i][1]:
            return False
        else:
            return True


def start_round_msg(round, num_dice=6):
    print(f'Starting round {round}')
    print(f"Rolling {num_dice} dice...")


class Game:
    def __init__(self, total_rounds=10):
        self.total_rounds = total_rounds
        self.current_round = 1
        self.banker = Banker()

    def welcome_game(self):
        print('Welcome to Ten Thousand')
        print('(y)es to play or (n)o to decline')
        choice = input("> ")
        if choice == 'y':
            for round in range(10):
                self.play_game(self.current_round)
            self.quit_game()
        else:
            print("OK. Maybe another time")

    def play_game(self, round):
        num_dice = 6
        score = 0
        start_round_msg(round, num_dice)
        while True:
            dice_list = GameLogic.roll_dice(num_dice)
            print(f"*** {display_roll(dice_list)} ***")
            if GameLogic.calculate_score(dice_list) == 0:
                zilch()
                self.banker.clear_shelf()
                self.current_round += 1
                num_dice = 6
                start_round_msg(self.current_round, num_dice)
                GameLogic.roll_dice(num_dice)

            else:
                kept_dice = self.get_dice_to_keep(dice_list, round)
                num_dice -= len(kept_dice)
                current_score = GameLogic.calculate_score(kept_dice)
                score += current_score

                print(f"You have {score} unbanked points and {num_dice} dice remaining")
                print("(r)oll again, (b)ank your points or (q)uit:")

                response = input("> ")
                if response == 'q':
                    self.quit_game()

                elif response == 'b':
                    self.banker.shelf(score)
                    self.banker.bank()
                    self.current_round += 1
                    self.round_end_msg(self.current_round, score)
                    break
                elif response == 'r':
                    if num_dice == 0:
                        num_dice = 6

    def get_dice_to_keep(self, dice_list, round):
        print("Enter dice to keep, or (q)uit:")
        response = input("> ")
        if response == 'q':
            self.quit_game()

        user_kept = []
        for char in response:
            if char.isnumeric():
                user_kept.append(int(char))
        return self.validate_kept(dice_list, user_kept, round)

    def round_end_msg(self, round, round_points):
        print(f"You banked {round_points} points in round {round - 1}")
        print(f"Total score is {self.banker.balance} points")

    def quit_game(self):
        print(f"Thanks for playing. You earned {self.banker.balance} points")
        sys.exit()

    def validate_kept(self, dice_list, user_kept, round):
        if validate_keepers(dice_list, user_kept):
            return user_kept
        else:
            print("Cheater!!! Or possibly made a typo...")
            print(f"*** {display_roll(dice_list)} ***")
            self.get_dice_to_keep(dice_list, round)


if __name__ == "__main__":
    game = Game()
    game.welcome_game()
