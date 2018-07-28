# Score categories
# Change the values as you see fit
def YACHT(dice):
    if len(set(dice)) == 1:
        print("yacht")
        return 50
    return 0

def ONES(dice):
    return dice.count(1)

def TWOS(dice):
    return dice.count(2) * 2

def THREES(dice):
    return dice.count(3) * 3

def FOURS(dice):
    return dice.count(4) * 4

def FIVES(dice):
    return dice.count(5) * 5

def SIXES(dice):
    return dice.count(6) * 6

def FULL_HOUSE(dice):
    total = 0
    counts = 0
    for i in set(dice):
        if dice.count(i) == 2 or dice.count(i) == 3:
            counts += dice.count(i)
            total += dice.count(i) * i
    if counts == 5:
        return total
    return 0

def FOUR_OF_A_KIND(dice):
    for i in set(dice):
        if dice.count(i) >= 4:
            return 4 * i
    return 0

def LITTLE_STRAIGHT(dice):
    for i in range(1, 6):
        if i not in dice:
            return 0
    return 30

def BIG_STRAIGHT(dice):
    for i in range(2, 7):
        if i not in dice:
            return 0
    return 30
def CHOICE(dice):
    return sum(dice)

def score(dice, category):
    return category(dice)
