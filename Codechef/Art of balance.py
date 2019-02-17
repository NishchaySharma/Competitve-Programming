import sys
def cal(n:int)->int:
    if n==1:
        return s_size-freq[-1]
    elif s_size%n==0:
        copy=freq[:]
        each=s_size//n
        res=0
        hold=0
        if f_size<n:
            for _ in range(n-f_size): copy.insert(0,0)
        back=len(copy)-1
        for i in range(n):
            if copy[back]>each:
                hold+=(copy[back]-each)
                res+=(copy[back]-each)
                copy[back]=each
            elif copy[back]<each:
                copy[back]+=hold
                hold=0
                if copy[back]>each: hold=copy[back]-each
                else:
                    res+=(each-copy[back])
                    copy[back]=each
            back-=1
            #print(copy,i,each,res,hold,back)
        return res
    else: return sys.maxsize
    
for _ in range(int(input())):
    s,freq,res,unique=input(),[],sys.maxsize,{}
    s_size=len(s)
    for i in s:
        if i not in unique: unique[i]=0
        unique[i]+=1
    for k in unique:
        freq.append(unique[k])
    freq.sort()
    f_size=len(freq)
    for i in range(1,27):
        if i>s_size: break
        res=min(res,cal(i))
        if res==0: break
    print(res)
