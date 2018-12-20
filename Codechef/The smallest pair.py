t=int(input())
for i in range(t):
    n=int(input())
    if n>0:
        lst=list(map(int,input().split()))
        lst=sorted(lst)
        print(lst[0]+lst[1])
        
