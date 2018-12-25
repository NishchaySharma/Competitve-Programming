with open('addin.txt','r') as file1:
    with open('addout.txt','w') as file2:
        file2.write(str(sum(map(int,file1.read().split()))))
