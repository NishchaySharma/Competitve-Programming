def recurr(r:int,c:int,k:int)->None:
    global count,move
    if k==0 or (r==0 and c==0) or (r==9 and c==9) or (r==0 and c==9) or (r==9 and c==0): return 
    else:
        k-=1
        if r>=1 and move[r][c]!=0:
            count+=1
            move[r][c]=0
            recurr(r-1,c,k)
        if r<=8 and move[r][c]!=0:
            count+=1
            move[r][c]=0
            recurr(r+1,c,k)
        if c>=1 and move[r][c]!=0:
            count+=1
            move[r][c]=0
            recurr(r,c-1,k)
        if c<=8 and move[r][c]!=0:
            count+=1
            move[r][c]=0
            recurr(r,c+1,k)
        if r>=1 and c>=1 and move[r][c]!=0:
            count+=1
            move[r][c]=0
            recurr(r-1,c-1,k)
        if r<=8 and c<=8 and move[r][c]!=0:
            count+=1
            move[r][c]=0
            recurr(r+1,c+1,k)
        if r<=8 and c>=1 and move[r][c]!=0:
            count+=1
            move[r][c]=0
            recurr(r+1,c-1,k)
        if r>=1 and c<=8 and move[r][c]!=0:
            count+=1
            move[r][c]=0
            recurr(r-1,c+1,k)
for _ in range(int(input())):
    count,move=1,[[1 for i in range(9)] for i in range(9)]
    r,c,k=map(int,input().split())
    move[r][c]=0
    recurr(r,c,k)
    print(count)
    for i in move:
        print(*i)
