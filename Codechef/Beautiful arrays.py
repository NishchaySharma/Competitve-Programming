for _ in range(int(input())):
    n,one,oneminus,other=int(input()),0,0,0
    for i in list(map(int,input().split())):
        if i==1: one+=1
        elif i==-1: oneminus+=1
        elif i!=0: other+=1
    if other>1 or (oneminus>1 and one==0) or (other!=0 and oneminus!=0): print('no')
    else: print('yes')
