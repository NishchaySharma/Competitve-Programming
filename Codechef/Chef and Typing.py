for _ in range(int(input())):
    n=int(input())
    left,right,word,done,time=['d','f'],['j','k'],[],{},0
    for i in range(n):
        word.append(input())
    for i in word:
        if i in done:
            time+=done[i]//2
        else:
            temp,pre=2,i[0]
            for j in i[1:]:
                if (j in left and pre in left) or (j in right and pre in right):
                    temp+=4
                else:
                    temp+=2
                pre=j
            time+=temp
            done[i]=temp
    print(time)
