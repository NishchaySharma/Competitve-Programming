for _ in range(int(input())):
    n,p=map(int,input().split())
    arr=list(map(int,input().split()))
    easy,hard=0,0
    for i in arr:
        if easy>1 or hard>2: break
        if i>=p//2: easy+=1
        if i<=p//10: hard+=1
    if easy==1 and hard==2 : print('yes')
    else: print('no')
