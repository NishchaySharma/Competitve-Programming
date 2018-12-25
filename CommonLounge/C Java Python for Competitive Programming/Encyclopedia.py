with open('encyin.txt','r') as file1:
    n,q=map(int,file1.readline().split())
    l=[]
    for _ in range(n):
        l.append(int(file1.readline()))
    with open('encyout.txt','w') as file2:
        for _ in range(q):
            file2.write(str(l[int(file1.readline())-1])+'\n')
