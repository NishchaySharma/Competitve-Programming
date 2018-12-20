n=int(input())
cmp,scr1,scr2=0,0,0
for i in range(n):
    p1,p2=map(int,input().split())
    scr1+=p1
    scr2+=p2
    if abs(cmp)<abs(scr1-scr2):
        cmp=scr1-scr2
if cmp>0:
    print("1",abs(cmp))
else:
    print("2",abs(cmp))
