import sys
for _ in range(int(input())):
    n, meal = int(input()), {'c':0,'o':0,'d':0,'e':0,'h':0,'f':0}
    for _ in range(n):
        x = input()
        for i in x:
            if i in meal: meal[i] += 1
    meal['c'] //= 2
    meal['e'] //= 2
    min_ = sys.maxsize
    for k in meal:
        if min_ > meal[k]:  min_ = meal[k]
    print(min_)
