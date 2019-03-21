for _ in range(int(input())):
    n=int(input())
    number=list(map(int,input().split()))
    result=1
    for i in range(1,n):
        if number[i]==1:    result=result*10 + 0
        else: result=result*10 + number[i]
    print(result)
