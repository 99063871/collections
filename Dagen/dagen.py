days = ["maandag", "dinsdag", "woensdag", "donderdag", "vrijdag", "zaterdag", "zondag"]

print("Alle dagen van de week zijn:")
for a in range(len(days)):
    print(days[a])

print("\nAlle werkdagen zijn:")
for a in range(5):
    print(days[a])

print("\nDe weekenddagen zijn:")
for a in range(5,7):
    print(days[a])

print("\nAlle dagen van de week in omgekeerde volgorde zijn:")
for a in range(6,-1,-1):
    print(days[a])

print("\nDe werkdagen in omgekeerde volgorde zijn:")
for a in range(4, -1, -1):
    print(days[a])

print("\nDe weekenddagen in omgekeerde volgorde zijn:")
for a in range(6,4,-1):
    print(days[a])