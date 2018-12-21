t=int(input())
cnt=0
for _ in range(t):
    x1,y1,x2,y2,x3,y3=map(int,input().split())
    side1=pow(x2-x1,2)+pow(y2-y1,2)
    side2=pow(x2-x3,2)+pow(y2-y3,2)
    side3=pow(x1-x3,2)+pow(y1-y3,2)
    if side1==side2+side3 or side2==side1+side3 or side3==side1+side2:
        cnt+=1
print(cnt)
