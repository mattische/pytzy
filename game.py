import dices
import scoreboard as sc




def startGame(player_list):
    """ starts a game. Supply each players name.
    """
    players = list()
    for p in player_list:
        players.append(p)

    sc.setPlayers(players)

def getPlayerNames():
    names = list()
    for n in sc.players:
        names.append(n["name"])
    return names


def playGame():
    p_index = 0 # player index
    turns = 1   # player turns - 3 rolls with the dices
    while p_index < len(sc.players):
        throws = 1
        print(sc.getPlayerName(p_index), "'s turn!")
        input("Throwing the dices!")

        while throws <= 3:
            dices.rollDices()

            print(sc.getPlayerName(p_index), " - throw ", throws,
                  " of 3.\nResult:\n", dices.dices)
            throws += 1

            saved_dices = rollDicesMenu()
            if len(saved_dices) > 0:
                print("You want to save these dices: ", saved_dices)
            input("press <enter> to throw again\n")

        p_index = p_index + 1

    p_index = 0

    print(p_index)

def rollDicesMenu():
    save = []
    nbr_dice = -1

    while nbr_dice != 0:
        nbr_dice = int(input("Save dice (1-6, 0=none, roll dices? "))
        if nbr_dice > 0:
            save.append(nbr_dice)

    print("Save dices: ", save)
    return save
