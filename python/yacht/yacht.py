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
    print((dice.pop()))
    dice = iter(dice)
    try:
        first = next(dice)
    except StopIteration:
        return True
    #print(all(first == rest for rest in dice)) ## DEBUG
    if all(first == rest for rest in dice):
        return 50
    else:
        return 0

if __name__ == "__main__":
    print(score([5,5,5,5,5],YACHT))
    print(score([5,5,5,5,4],YACHT))
    score([5,2,4,1,4],YACHT)
    score([5,1,3,1,4],YACHT)
    score([5,1,4,4,4],YACHT)
    score([5,1,4,1,4],YACHT)
    score([5,1,4,1,4],YACHT)