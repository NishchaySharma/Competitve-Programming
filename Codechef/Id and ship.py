t=int(input())
for i in range(t):
    char=input()
    d={'b':'BattleShip','c':'Cruiser','d':'Destroyer','f':'Frigate'}
    if ord(char) < 91:
        char=chr(ord(char)+32)
    print(d[char])
