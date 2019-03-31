t,convert=input().split()
d={chr(i+97):convert[i].lower() for i in range(26)}
for _ in range(int(t)):
    a=input()
    for i in a:
        if i=='_': print(' ',end='')
        elif not i.isalpha(): print(i,end='')
        elif i!=i.lower(): print(d[i.lower()].upper(),end='')
        else: print(d[i],end='')
    print()
