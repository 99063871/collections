import random

list = ["oranje", "blauw", "groen", "bruin"]
bag = [0, 0, 0, 0]

mnmDictionaryBag = {
    "oranje" : 0,
    "blauw" : 0, 
    "groen" : 0, 
    "bruin" : 0
}



def func(hoeveel):
    for a in range(hoeveel):
        number = random.randint(0, 3)
        if number == 0:
            mnmDictionaryBag["oranje"] += 1
            bag[0] += 1
        elif number == 1:
            mnmDictionaryBag["blauw"] += 1
            bag[1] += 1
        elif number == 2:
            mnmDictionaryBag["groen"] += 1
            bag[2] += 1
        else:
            mnmDictionaryBag["bruin"] += 1
            bag[3] += 1
    return mnmDictionaryBag

func(20)
for key, value in mnmDictionaryBag.items():
    print(key, ':', value)
for x in range(0,4):
    print(bag[x],"van",list[x])