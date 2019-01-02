for _ in range(int(input())):
    n=int(input())
    l=[]
    for i in range(n):
        l.append([])
        for j in range(n):
            l[i].append(0)
    l[0][0],i,j,jc,count=1,0,1,1,1
    while jc!=n:
        count+=1
        l[i][j]=count
        if j==0:
            jc+=1
            j=jc
            i=0
        else:
            j-=1
            i+=1
    i,j,ic=1,n-1,1
    while ic!=n:
        count+=1
        l[i][j]=count
        if i==n-1:
            ic+=1
            i=ic
            j=n-1
        else:
            j-=1
            i+=1
    for i in l:
        for j in i:
            print(j,end=' ')
        print()
