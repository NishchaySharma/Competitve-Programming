for _ in range(int(input())):
    n=int(input())
    arr=sorted(list(map(int,input().split())))
    res=0
    for i in range(n//2):
        res+=abs(arr[i]-arr[n-i-1])
    print(res)
