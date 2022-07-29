from random import randint
from collections import Counter


def default_dice_roller():
    return randint(1, 6), randint(1, 6)


def dice_roller_4_3():
    return 4, 3


class GameLogic:
    def __init__(self):
        pass

    @staticmethod
    def roll_dice(value):
        dice_list = []
        while len(dice_list) != value:
            dice_list.append(randint(1, 6))
        return tuple(dice_list)

    @staticmethod
    def calculate_score(dice):  # dice is a tuple of ints from user dice roll
        if len(dice) > 6:
            raise Exception
        counts = Counter(dice)
        if len(counts) == 6:  # 1, 2, 3, 4, 5, 6
            return 1500
        if len(counts) == 3 and all(val == 2 for val in counts.values()):
            return 1500
        score = 0
        ones_used = False
        fives_used = False
        for num in range(1, 7):
            a_count = counts[num]
            if a_count >= 3:
                if num == 1:
                    ones_used = True
                elif num == 5:
                    fives_used = True
                    score += num * 100
                    # handle 4,5,6 of a kind
                    a_beyond_3 = a_count - 3
                    score += score * a_beyond_3
                    if num == 1:
                        score *= 100
        if not ones_used:
            score += counts.get(1, 0) * 100
        if not fives_used:
            score += counts.get(5, 0) * 50
        return score

    def play_dice(self):
        while True:
            print("Enter r to roll or q to quit")
            choice = input("> ")
            if choice == "q":
                print("OK, bye")
                break
            elif choice == "r":
                roll = self
                values_in_roll = []
                for value in roll:
                    values_in_roll.append(str(value))
                formatted_roll = " ".join(values_in_roll)
                print(f"*** {formatted_roll} ***")

    @staticmethod
    def validate_keepers(roll, user_input):
        roll_most_common = Counter(roll).most_common()
        input_most_common = Counter(user_input).most_common()
        for i in range(len(input_most_common)):
            if input_most_common[i][1] > roll_most_common[i][1]:
                return False
            else:
                return True

    if __name__ == '__main__':
        play_dice(dice_roller_4_3)
