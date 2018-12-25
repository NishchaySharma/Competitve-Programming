with open('tripin.txt','r') as file1:
    n=int(file1.readline())
    count,position=0,[]
    for i in range(n):
        if int(file1.readline())%3==0:
            count+=1
            position.append(i+1)
    with open('tripout.txt','w') as file2:
        if count==0:
            file2.write('Nothing here!')
        else:
            file2.write(str(count)+'\n')
            for i in position:
                file2.write(str(i)+' ')
