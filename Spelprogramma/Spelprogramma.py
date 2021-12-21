import random

spelList = ['Monopoly', 'Yathzee', 'Bridge', 'Poker', 'Pesten', 'Mens erger je niet', 'Cluedo']
gameList = []
def spelProgramma(list, minimum, maximum):
    totalAmount = random.randint(minimum,maximum)
    for a in range(totalAmount):
        amount = len(spelList) - 1
        games = random.randint(0, amount)
        game = spelList[games]
        gameList.append(game)
    return gameList

print(spelProgramma(gameList, 3, 10))