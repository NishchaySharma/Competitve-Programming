with open('countin.txt','r') as file1:
    with open('countout.txt','w') as file2:
        for i in range(1,int(file1.read())+1):
            file2.write(str(i)+'\n')
