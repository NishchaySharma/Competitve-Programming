with open('sitin.txt') as value:
    r,s=map(int,value.readline().split())
    book=int(value.readline())
    flag=True
    if book<=r*s:
        flag=False
    with open('sitout.txt','w') as store:
        if flag:
            store.write(str(r*s)+' '+str(book-r*s))
        else:
            store.write(str(book)+' 0')
