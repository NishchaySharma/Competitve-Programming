while True:
    try:
        n=int(input())
        if n<(n//2 + n//3 + n//4):
            print(n//2 + n//3 + n//4)
        else:
            print(n)
    except EOFError:
        break
