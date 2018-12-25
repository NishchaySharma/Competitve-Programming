with open('dictin.txt','r') as file1:
    d,w=map(int,file1.readline().split())
    hold={}
    for _ in range(d):
        key,val=map(int,file1.readline().split())
        hold[key]=val
    with open('dictout.txt','w') as file2:
        for _ in range(w):
            tmp=int(file1.readline())
            if tmp not in hold:
                file2.write('C?\n')
            else:
                file2.write(str(hold[tmp])+'\n')
    
