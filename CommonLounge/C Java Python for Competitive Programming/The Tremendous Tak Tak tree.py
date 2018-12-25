with open('taktakin.txt','r') as file1:
    value=int(file1.read())
    count=0
    while (value-1)%11!=0:
        value*=2
        count+=1
    with open('taktakout.txt','w') as file2:
        file2.write(str(count)+' '+str(value))
