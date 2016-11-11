from random import randint


dices = [0, 0, 0, 0, 0]


def rollDices():
    """ rolls all dices, generates random int 0 >=< 6
    """
    for i in range(5):
        dices[i] = randint(1, 6)


def rollSpecificDices(*indexes):
    for ind in indexes:
        if ind <= 4 and ind >= 0:
            dices[ind] = randint(1,6)
