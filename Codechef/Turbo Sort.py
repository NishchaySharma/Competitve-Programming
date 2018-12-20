t=int(input())
lst=[]
for i in range(t):
    n=int(input())
    lst.append(n)
lst=sorted(lst)     #timsort algo
for i in lst:
    print(i)
