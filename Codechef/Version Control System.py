t=int(input())
for test in range(t):
    n,m,k=map(int,input().split())
    m_list=set(map(int,input().split()))
    k_list=set(map(int,input().split()))
    n_list={i for i in range(1,n+1)}
    res1=m_list.intersection(k_list)
    res1=len(res1) if res1.__len__()!=0 else 0
    res2=n_list.difference(m_list).intersection(n_list.difference(k_list))
    res2=len(res2) if res2.__len__()!=0 else 0
    print(res1,res2)
