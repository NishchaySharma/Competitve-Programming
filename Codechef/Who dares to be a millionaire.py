for _ in range(int(input())):
    n,ca,ga,w,count=int(input()),input(),input(),list(map(int,input().split())),0
    if ca==ga:
        print(w[n])
    else:
        for i in range(n):
            if ca[i]==ga[i]: count+=1
        print(max(w[:count+1]))
