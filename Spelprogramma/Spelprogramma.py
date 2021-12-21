import random

spelList = ['Monopoly', 'Yathzee', 'Bridge', 'Poker', 'Pesten', 'Mens erger je niet', 'Cluedo']
gameList = []

def spelProgramma(list):
    totalAmount = random.randint(3,10)
    for a in range(totalAmount):
        amount = len(spelList) - 1
        games = random.randint(0, amount)
        game = spelList[games]
        gameList.append(game)
    return gameList

print(spelProgramma(gameList))