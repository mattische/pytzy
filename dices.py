from random import randint


dices = list()


def setupDices():
    dices = list()
    for i in range(5):
        dices.append(0)



def rollDices():
    """ rolls all dices, generates random int 0 >=< 6
    """
    for i in range(5):
        dices[i] = randint(0, 6)


def rollSpecificDices(*indexes):
    for ind in indexes:
        if ind <= 4 and ind >= 0:
            dices[ind] = randint(0,6)
        


