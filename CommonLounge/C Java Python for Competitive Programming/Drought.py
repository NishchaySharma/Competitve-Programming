with open('rainin.txt','r') as file1:
    n,c=map(int,file1.readline().split())
    day=0
    for _ in range(n):
        if c>0:
            c-=int(file1.readline())
            day+=1
        else:
            break
    with open('rainout.txt','w') as file2:
        file2.write(str(day))
