t=int(input())
for _ in range(t):
    name=list(input().split())
    for i in range(len(name)-1):
        name[i]=name[i][0].upper()
        name[i]+='.'
    name[-1]=name[-1].lower()
    name[-1]=name[-1][0].upper()+name[-1][1::]
    for i in name:
        print(i,end=' ')
    print()
