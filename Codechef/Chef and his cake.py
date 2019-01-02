for _ in range(int(input())):
    n,m=map(int,input().split())
    l,tmp1,tmp2=[],[],[]
    for i in range(n):
        l.append(list(input()))
    pre1,pre2='R','G'
    for i in range(n):
        tmp1.append([])
        tmp2.append([])
        if i!=0 and m%2==0:
            pre1,pre2=pre2,pre1
        for j in range(m):
            if pre1=='R':
                tmp1[i].append('G')
                pre1='G'
            else:
                tmp1[i].append('R')
                pre1='R'
            if pre2=='R':
                tmp2[i].append('G')
                pre2='G'
            else:
                tmp2[i].append('R')
                pre2='R'
    count1,count2=0,0
    for i in range(n):
        for j in range(m):
            if l[i][j]!=tmp1[i][j]:
                if tmp1[i][j]=='R':
                    count1+=3
                else:
                    count1+=5
            if l[i][j]!=tmp2[i][j]:
                if tmp2[i][j]=='R':
                    count2+=3
                else:
                    count2+=5
    print(min(count1,count2))
