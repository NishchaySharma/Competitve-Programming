s=input()
n=int(input())
for _ in range(n):
    w=input()
    cnt=0
    for i in w:
        if i in s:
            cnt+=1
    if cnt==len(w):
        print('Yes')
    else:
        print('No')
