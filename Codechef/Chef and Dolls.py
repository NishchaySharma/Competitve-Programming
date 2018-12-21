#each type of doll has a index in l where l[0] will always be empty!
t=int(input())
for i in range(t):
    n=int(input())
    l=[0]*1000001
    for j in range(n):
        l[int(input())]+=1
    for j in l:
        if j%2!=0:
            break
    print(l.index(j))
