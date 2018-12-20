t=int(input())
for i in range(t):
    dic={'A':1,'B':2,'D':1,'O':1,'P':1,'Q':1,'R':1}
    l1=['A','D','O','P','Q','R']
    l2=['B']
    val=input()
    count=0
    for i in val:
        if i in l1:
            count+=1
        elif i in l2:
            count+=2
    print(count)
