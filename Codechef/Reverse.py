t=int(input())
for i in range(t):
    j=int(input())
    rev=0
    while j>0:
        rev*=10
        rev+=j%10
        j//=10
    print(rev)
