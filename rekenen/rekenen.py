listOne = [1,2,3,4,5,6,7,8,9,10]
listTwo = [2,4,6,8,10,12,14,16,18,20]

def addAndDisplayLists():
    print("---------\nAdd Lists")
    for a in range(len(listOne)):
        anwser = listOne[a]+listTwo[a]
        print(listOne[a], "+", listTwo[a], "=", anwser)

def substractAndDisplayLists():
    print("\n---------------\n Substract lists")
    for a in range(len(listOne)):
        anwser = listOne[a]-listTwo[a]
        print(listOne[a], "-", listTwo[a], "=", anwser)


def multiplyAndDisplayLists():
    print("\n--------------\nMultiply lists")
    for a in range(len(listOne)):
        anwser = listOne[a]*listTwo[a]
        print(listOne[a], "*", listTwo[a], "=", anwser)

def divideAndDisplayLists():
    print("\n-------------\nDivide lists")
    for a in range(len(listOne)):
        anwser = listOne[a]/listTwo[a]
        print(listOne[a], "/", listTwo[a], "=", anwser)

addAndDisplayLists()
substractAndDisplayLists()
multiplyAndDisplayLists()
divideAndDisplayLists()