for _ in range(int(input())):
    n=int(input())
    cw,s,e,em,m,mh,h=0,0,0,0,0,0,0
    for _ in range(n):
        x=input()
        if x=='cakewalk': cw+=1
        elif x=='simple': s+=1
        elif x=='easy': e+=1
        elif x=='easy-medium': em+=1
        elif x=='medium': m+=1
        elif x=='medium-hard': mh+=1
        else: h+=1
    if cw>=1 and s>=1 and e>=1 and (em>=1 or m>=1) and (mh>=1 or h>=1): print('Yes')
    else: print('No')
