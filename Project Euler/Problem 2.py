first,second,current=1,2,3
res=2
while current<4000000:
    print(first,second,current)
    if current%2==0:
        res+=current
    first=second
    second=current
    current=first+second
print(res)
