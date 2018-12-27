for _ in range(int(input())):
    tr=int(input())
    trarr=set(map(int,input().split()))
    dr=int(input())
    drarr=set(map(int,input().split()))
    ts=int(input())
    tsarr=set(map(int,input().split()))
    ds=int(input())
    dsarr=set(map(int,input().split()))
    trsinter=tsarr.difference(trarr)
    drsinter=dsarr.difference(drarr)
    if len(trsinter)==0 and len(drsinter)==0:
        print('yes')
    else:
        print('no')
