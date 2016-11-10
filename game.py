import dices
import scoreboard as sc




def startGame(*player_names):
    """ starts a game. Supply each players name.
    """
    players = list()
    for p in player_names:
        players.append(p)

    sc.setPlayers(players)

def getPlayerNames():
    names = list()
    for n in sc.players:
        names.append(n["name"])


def playGame():
    p_index = 0
    turns = 1
    while p_index < 3:
        p_index = 0
        throws = 1
        print(sc.getPlayerName(p_index), " turn!")
        input("Throw the dices!")
        dices.setupDices()
        while throws <= 3:
            dices.rollDices()
            print("Throw ", throws, " of 3. Result:\n", dices.dices)
            throws += 1
        p_index += 1



    
