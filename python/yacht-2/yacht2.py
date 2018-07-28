# Score categories
# Change the values as you see fit

from collections import Counter

# YACHT = f_yacht


def score(dice, category):
    def getValues(l):
        return Counter(l).most_common().sort(key=lambda x: x[1])

    def f_yacht(dice):
        dice_dict = Counter(dice)
        if dice_dict[dice[0]] == 5:
            return 50
        return 0

    def fullHouse(dice):
        values = getValues(dice)
        if len(values) == 2:
            if values[0][1] == 2 and values[1][1] == 3:
                return sum(dice)
        return 0

    def poker(dice):
        values = getValues(dice)
        for v in values:
            if v[1] >= 4:
                return v[0] * 4
        return 0

    def order(dice):
        dice.sort()
        ant = 0
        for n in dice:
            if ant < n:
                ant = n
            else:
                return False
        return True


    def number(count, n):
        if n in count:
            return n * count[n]
        else:
            return 0

    def category(dice):
        ONES =  lambda x: number(Counter(x),1)
        TWOS = lambda x: number(Counter(x),2)
        THREES = lambda x: number(Counter(x),3)
        FOURS = lambda x: number(Counter(x),4)
        FIVES = lambda x: number(Counter(x),5)
        SIXES = lambda x: number(Counter(x),6)
        FULL_HOUSE = fullHouse
        FOUR_OF_A_KIND = poker
        LITTLE_STRAIGHT = lambda x: 30 if order(x) and (5 in x and 1 in x) else 0
        BIG_STRAIGHT = lambda x: 30 if order(x) and (6 in x and 2 in x) else 0
        CHOICE = lambda x: sum(x)
        YACHT = f_yacht
        return dice

   
    return category(dice)

