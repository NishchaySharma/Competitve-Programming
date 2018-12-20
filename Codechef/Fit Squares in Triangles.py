t=int(input())
for test in range(t):
    b=int(input())
    if b>3:
        print((b-2)//2*((b-2)//2 + 1)//2)
    else:
        print(0)
