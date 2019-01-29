for _ in range(int(input())):
    l,r=map(int,input().split())
    tot=r+1-l
    if l%2==1:  #If tot is 4*n+1 or 4n+2 (n>=0) then parity same as of l
        if (tot-1)%4==0 or (tot-2)%4==0: print('Even' if l%2==0 else 'Odd')
        else: print('Odd' if l%2==0 else 'Even')
    else:   #Parity of result is same as l if
        if tot==1: print('Even' if l%2==0 else 'Odd')
        elif (tot-2)%4==0 or (tot-3)%4==0: print('Even' if l%2==1 else 'Odd')
        else: print('Odd' if l%2==1 else 'Even') 
