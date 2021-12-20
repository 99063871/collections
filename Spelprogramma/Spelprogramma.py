import random

spelList = ['Monopoly', 'Yathzee', 'Bridge', 'Poker', 'Pesten', 'Mens erger je niet', 'Cluedo']

def spelProgramma():
    totalAmount = random.randint(3,10)
    for a in range(totalAmount):
        amount = len(spelList) - 1
        games = random.randint(0, amount)
        print(spelList[games])

spelProgramma()