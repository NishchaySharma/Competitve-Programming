t=int(input())
for i in range(t):
    s=list(input())
    res=[]
    stack=[]
    alpha=[j for j in range(65,91)]
    alpha+=[j for j in range(97,123)]
    for j in s:
        if j=='(':
            continue
        elif ord(j) in alpha:
            res.append(j)
        elif j==')':
            res.append(stack.pop())
        else:
            stack.append(j)
    res=''.join(res)
    print(res)
