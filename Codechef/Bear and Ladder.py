q=int(input())
for _ in range(q):
    a,b=map(int,input().split())
    minn=min(a,b)
    maxx=max(a,b)
    if minn+1==maxx or minn+2==maxx:
        if (minn%2==0 and maxx%2==0) or (minn%2==1 and maxx%2==0) or (minn%2==1 and maxx%2==1):
            print('YES')
        else:
            print('NO')
    else:
        print('NO')
 
