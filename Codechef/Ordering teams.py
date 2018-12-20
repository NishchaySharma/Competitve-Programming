def compare(l1:list,l2:list,l3:list)->bool:
    if l1[0]>=l2[0] and l1[1]>=l2[1] and l1[2]>=l2[2]:
        if l1[0]>l2[0] or l1[1]>l2[1] or l1[2]>l2[2]:
            if l2[0]>=l3[0] and l2[1]>=l3[1] and l2[2]>=l3[2]:
                if l2[0]>l3[0] or l2[1]>l3[1] or l2[2]>l3[2]:
                    return True
        else:
            return False
t=int(input())
for test in range(t):
    p1=list(map(int,input().split()))
    p2=list(map(int,input().split()))
    p3=list(map(int,input().split()))
    if compare(p1,p2,p3) or compare(p1,p3,p2) or compare(p2,p1,p3) or compare(p2,p3,p1) or compare(p3,p1,p2) or compare(p3,p2,p1):
        print('yes')
    else:
        print('no')
