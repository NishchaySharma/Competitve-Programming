n=int(input())
q=int(input())
l=[0]*100000
tmp=1
for i in range(q):
    a,b,c=map(int,input().split())
    if a==0:
        if l[b-1]==0:
            if l[c-1]==0:
                l[b-1],l[c-1]=tmp,tmp
                tmp+=1
            else:
                l[b-1]=l[c-1]
        elif l[c-1]==0:
            l[c-1]=l[b-1]
        else:
            for j in l:
                if i==l[c-1]:
                    l[l.index(i)]=l[b-1]
    if a==1:
        if l[b-1]==l[c-1]:
            print("YES")
        else:
            print("NO")
                        
