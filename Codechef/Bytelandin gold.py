while True:
    try:
        n=int(input())
    except:
        exit()
    res=n//2+n//3+n//4
    print(res if res>n else n)
