t=int(input())
for i in range(t):
    n=int(input())
    val=1
    for i in range(1,n+1,1):
        val*=i
    print(val)
