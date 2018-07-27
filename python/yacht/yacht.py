# Score categories
# Change the values as you see fit
YACHT = None
ONES = None
TWOS = None
THREES = None
FOURS = None
FIVES = None
SIXES = None
FULL_HOUSE = None
FOUR_OF_A_KIND = None
LITTLE_STRAIGHT = None
BIG_STRAIGHT = None
CHOICE = None

def score(dice, category):
    if not category(dice):
        return 0
    return category(dice)
    
def YACHT(dice):
    return 0

if __name__ == "__main__":
    print(score([5,5,5,5,5],YACHT))
