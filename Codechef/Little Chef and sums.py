for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    print(arr.index(min(arr))+1)