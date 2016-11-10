players = list() #the players





def setPlayers(playerList):
    """ Creates players on the scoreboard;
        players are in a list(), each player on each index.
        On every index there is a dict;
        'name' - the name of the player
        'score' - a dict with points
    """

    for player in playerList:
        player_data = {"name": player, "score": createScoreList()}
        players.append(player_data)

    print(players[0]["name"])



def createScoreList():
    """ creates, and returns, a dict with possible scoer names in yatzy.
    """
    scores = {"Ones": 0, 
              "Twos": 0, 
              "Threes": 0,
              "Fours": 0,
              "Fives": 0,
              "Sixths": 0,
              "One pair": 0,
              "Two pair": 0,
              "Three of a kind": 0,
              "Four of a kind": 0,
              "House": 0,
              "Small ladder": 0,
              "Large ladder": 0,
              "Chance": 0,
              "Yatzy": 0}
    return scores

            
def insertScore(player_index, score_list_name, points):
    """ insert a score for a cetain score-name and a certain player
    """
    
    if player_index >= len(players):
       return False

    players[player_index]["score"][score_list_name] = points
    return getPlayerTotal(player_index)


def calcPlayerTotal(player_index):
    """ calculate total score for a certain player
    """
    if player_index >= len(players):
       return False

    temp = 0
    for points in players[player_index]["score"].values():
        temp += points

    return temp


def getPlayerTotal(player_index):
    """ get the total scoer of a player
    """
    if player_index >= len(players):
       return False
       
    return calcPlayerTotal(player_index)


    
def getPlayerName(index):
    return players[index]["name"]
