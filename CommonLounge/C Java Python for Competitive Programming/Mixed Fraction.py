with open('mixin.txt','r') as file1:
    n,d=map(int,file1.read().split())
    flag=True
    if n%d==0:
        flag=False
    with open('mixout.txt','w') as file2:
        if flag:
            file2.write(str(n//d)+' '+str(n%d)+'/'+str(d))
        else:
            file2.write(str(n//d))
