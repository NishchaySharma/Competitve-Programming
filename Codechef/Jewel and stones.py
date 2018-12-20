t=int(input())
for test in range(t):
    j=input()
    s=list(input())
    cnt=0
    for i in s:
        if i in j:
            cnt+=1
    print(cnt)
