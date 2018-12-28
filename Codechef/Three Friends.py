def check(x:int,y:int,z:int)->bool:
    return x+y+z==0
for _ in range(int(input())):
    x,y,z=map(int,input().split())
    if check(x,y,z) or check(x,y,-z) or check(x,-y,z) or check(x,-y,-z) or check(-x,y,z) or check(-x,y,-z) or check(-x,-y,z) or check(-x,-y,-z):
        print('yes')
    else:
        print('no')
