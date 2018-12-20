print('Enter size: ',end='')
size=int(input())
lst=[]
print('Enter elements: ')
for i in range(size):
    num=int(input())
    lst.append(num)
print('Order before sort: ',end='')
for i in lst:
    print(i,end=' ')
print()
for i in range(size-1):
    pos=i
    for j in range(i+1,size):
        if lst[j]<lst[pos]:
            pos=j
    if pos!=i:
        tmp=lst[i]
        lst[i]=lst[pos]
        lst[pos]=tmp
print('After sorting: ',end='')
for i in lst:
    print(i,end=' ')
