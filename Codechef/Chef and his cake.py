t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    s=''
    for i in range(n):
        s+=input()
    s=list(s)
    cost1,cost2,store=0,0,s[:]
    if m%2==1:
        tmp=0
        for i in range(1,n*m):
            if s[i]==s[i-1]:
                if s[i]=='R':
                    s[i]='G'
                    tmp+=3
                else:
                    s[i]='R'
                    tmp+=5
        s=store
        cost1,tmp=tmp,0
        if s[0]=='R':
            s[0]='G'
            tmp+=3
        else:
            s[0]='R'
            tmp+=5
        for i in range(1,n*m):
            if s[i]==s[i-1]:
                if s[i]=='R':
                    s[i]='G'
                    tmp+=3
                else:
                    s[i]='R'
                    tmp+=5

        cost2=tmp
        print(cost1 if cost1<cost2 else cost2)
    else:
        tmp=0
        for i in range(1,n*m):
            if i%m==0:
                if s[i]!=s[i-1]:
                    if s[i]=='R':
                        s[i]='G'
                        tmp+=3
                    else:
                        s[i]='R'
                        tmp+=5
            elif s[i]==s[i-1]:
                if s[i]=='R':
                    s[i]='G'
                    tmp+=3
                else:
                    s[i]='R'
                    tmp+=5
        s=store
        cost1,tmp=tmp,0
        if s[0]=='R':
            s[0]='G'
            tmp+=3
        else:
            s[0]='R'
            tmp+=5
        for i in range(1,n*m):
            if i%m==0:
                if s[i]!=s[i-1]:
                    if s[i]=='R':
                        s[i]='G'
                        tmp+=3
                    else:
                        s[i]='R'
                        tmp+=5
            elif s[i]==s[i-1]:
                if s[i]=='R':
                    s[i]='G'
                    tmp+=3
                else:
                    s[i]='R'
                    tmp+=5
        cost2=tmp
        print(cost1 if cost1<cost2 else cost2)
