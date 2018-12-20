t=int(input())
tmp=t/2
l=list(map(int,input().split()))
for i in l:
    if i%2==0:
        t-=1
if t<tmp:
    print('READY FOR BATTLE')
else:
    print('NOT READY')
