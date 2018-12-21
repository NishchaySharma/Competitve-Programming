t=int(input())
for _ in range(t):
    s=list(input())
    chef,other=0,0
    while len(s)!=0:
        i=s.pop(0)
        if i=='1':
            chef+=1
        else:
            other+=1
        if chef==11 and other<=9:
            flag=True
            break
        elif chef<=9 and other==11:
            flag=False
            break
        elif chef==10 and other==10:
            tie=0
            while len(s)!=0:
                i=s.pop(0)
                if i=='1':
                    tie+=1
                else:
                    tie-=1
                if tie==2:
                    flag=True
                    break
                elif tie==-2:
                    flag=False
                    break
            break
    print('WIN' if flag else 'LOSE')
