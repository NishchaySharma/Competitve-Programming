for _ in range(int(input())): 
    n,m=map(int,input().split())
    a,b=n-n%m,n+(m-n%m)
    if abs(a-n)==abs(b-n): 
        print(a if abs(a)>abs(b) else b) 
    else: print(a if abs(a-n)<abs(b-n) else b)
