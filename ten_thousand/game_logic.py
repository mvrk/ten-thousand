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
    def get_scorers(dice):
        dice_list = []
        for num in dice:
            if num == 1:
                dice_list.append(num)
            elif num == 5:
                dice_list.append(num)
        return tuple(dice_list)

    @staticmethod
    # Calculate score based on presented rolled values.
    def calculate_score(roll):
        score = 0
        # before roll
        if roll is None:
            roll = [0]

        # rolled, sort numbers by  their values
        count_dice = Counter(roll)

        # if rolled out 1, 2, 3, 4, 5, 6
        if len(count_dice) == 6:
            return 1500

        # if rolled out 3 pairs, i.e: 2, 2, 3, 3, 6, 6
        if len(roll) == 6 and len(count_dice) == 3:
            return 1500

        else:
            for i in range(1,7):
                count = count_dice[i]
                if i == 1:
                    if count >= 3:
                        score += (count - 2) * 1000
                    else:
                        score += count * 100
                elif i == 5:
                    if count >= 3:
                        score += (count - 2) * 500
                    else:
                        score += count * 50
                else:
                    if count >= 3:
                        score += i * (count - 2) * 100
        return score

    # @staticmethod
    # def get_scorers(dice):
    #     dice_list = []
    #     for num in dice:
    #         if num == 1:
    #             dice_list.append(num)
    #         elif num == 5:
    #             dice_list.append(num)
    #     return tuple(dice_list)


