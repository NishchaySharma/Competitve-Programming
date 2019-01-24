pweight={chr(65+i):1+i for i in range(26)}
pweight['"'],pweight["'"]=0,0
with open('names.txt') as file1:
    data,res=[],0
    for i in file1:
        data+=i.split(',')
        break
    data=sorted(data)
    for i in range(len(data)):
        for j in data[i]:
            res+=(pweight[j]*(i+1))
    print(res)
