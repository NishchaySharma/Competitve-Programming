d,pos={1:1,2:1},2
def generate(n:int)->None:
    global pos
    start=pos+1
    pos=n
    for i in range(start,n+1):
        d[i]=d[i-1]+d[i-2]
for _ in range(int(input())):
    n=int(input())
    if n not in d:
        generate(n)
    print(d[n])
