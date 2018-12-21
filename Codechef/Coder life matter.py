t=int(input())
for test in range(t):
    l=list(map(int,input().split()))
    cnt=0
    for i in range(30):
        cnt=0
        if l[i]==1:
            while i<30 and l[i]==1:
                cnt+=1
                i+=1
            if cnt>5:
                break
    if cnt>5:
        print('#coderlifematters')
    else:
        print('#allcodersarefun')
