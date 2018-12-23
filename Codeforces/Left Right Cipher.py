import math
s=list(input())
move,pos,change=True,math.ceil(len(s)/2)-1,1
res=s[pos]
while len(res)!=len(s):
    if move:
        pos+=change
        move=False
    else:
        pos-=change
        move=True
    change+=1
    res+=s[pos]
print(res)
