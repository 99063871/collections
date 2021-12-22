import random
list = ["oranje", "blauw", "groen", "bruin"]
bag = [0, 0, 0, 0]
def func(hoeveel):
    for a in range(hoeveel):
        number = random.randint(0, 3)
        if number == 0:
            bag[0] += 1
        elif number == 1:
            bag[1] += 1
        elif number == 2:
            bag[2] +=1
        else:
            bag[3] += 1
    return bag

func(20)
for x in range(0,4):
    print(bag[x],"van",list[x])