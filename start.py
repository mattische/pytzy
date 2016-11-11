import game

nbr = int(input("How many players? "))
p_names = []
i = 0
"""
while i < nbr:
    p_names[i] = input("Name of player ", (i+1), ": ")
    i += 1
"""
p_names = ["Arne", "Leif"]
game.startGame(p_names)
print("Players: ", game.getPlayerNames())
game.playGame()
