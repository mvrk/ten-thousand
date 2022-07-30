from random import randint
from collections import Counter


class GameLogic:
    def __init__(self):
        pass

    @staticmethod
    def roll_dice(num_dice):
        dice_list = []
        while len(dice_list) != num_dice:
            dice_list.append(randint(1, 6))
        return tuple(dice_list)

    @staticmethod
    # Calculate score based on presented rolled values.
    def calculate_score(roll):
        score = 0
        # before roll
        if roll is None:
            roll = [0]

        # rolled, sort numbers by  their values
        count_dice = Counter(roll).most_common()

        # if rolled out 1, 2, 3, 4, 5, 6
        if len(count_dice) == 6:
            return 1500

        # if rolled out 3 pairs, i.e: 2, 2, 3, 3, 6, 6
        if len(roll) == 6 and len(count_dice) == 3:
            return 1500

        else:
            for i in range(len(count_dice)):
                number = count_dice[i][0]
                common = count_dice[i][1]
                base = number * 100
                # handle 1' score pattern
                if number == 1:
                    if common > 2:
                        base = number * 1000
                    else:
                        score += base * common
                # handle 5' score pattern
                if number == 5:
                    if common == 1:
                        score = 50
                    if common == 2:
                        score = 100
                # handle 2, 3, 4, 6
                if common > 2:
                    score += base * (common - 2)
        return score
