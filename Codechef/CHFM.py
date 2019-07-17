t = input()
t = int(t)
while t>0:
    n = input()
    n = int(n)
    s = input()
    l = []
    tot = 0
    for i in s.split(" "):
        i = int(i)
        l.append(i)
        tot += i
    avg = tot/n 
    flag = True
    for i in range(n):
        if l[i] == avg:
            flag = False
            print(i+1)
            break
    if flag: print('Impossible')
    t-=1
