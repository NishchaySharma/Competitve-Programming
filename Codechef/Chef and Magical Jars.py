# Author Nishchay Sharma
for _ in range(int(input())):
    n=int(input())
    arr,res=list(map(int,input().split())),0
    for i in arr: res+=(i-1)
    print(res+1)
