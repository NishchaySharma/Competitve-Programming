with open('bendin.txt','r') as file1:
    x1,y1,x2,y2=map(int,file1.readline().split())
    x3,y3,x4,y4=map(int,file1.readline().split())
    if x1>x3:
        left=x1
    else:
        left=x3
    if x2<x4:
        right=x2
    else:
        right=x4
    if y1>y3:
        down=y1
    else:
        down=y3
    if y2<y4:
        up=y2
    else:
        up=y4
    if left<right and up>down:
        intersection=abs(up-down)*abs(left-right)
    else:
        intersection=0
    total=abs(x2-x1)*abs(y2-y1)+abs(x3-x4)*abs(y3-y4)
    with open('bendout.txt','w') as file2:
        file2.write(str(total-intersection))
