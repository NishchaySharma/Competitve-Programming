print('Enter size: ',end='')
length=int(input())
lst=[]
print('Enter elements: ')
for i in range(length):
    n=int(input())
    lst.append(n)
print('You entered: ',end='')
for i in lst:
    print(i,end=' ')
print()
for i in range(1,length):
    j=i
    key=lst[i]
    while j>0 and key<lst[j-1]:
        lst[j]=lst[j-1]
        j-=1
    lst[j]=key
print('Sorted elements: ',end='')
for i in lst:
    print(i,end=' ')
