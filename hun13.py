q,w1=map(int,input().split())
ll1=[]
s1=[]
a1=[int(m) for m in input().split() ]
for i in range(0,n1):
    u1,v1=map(int,input().split())
    for j in range(u1-1 ,v1):
        s1.append(a1[j])
    x1=sorted(s1)
    ll1.append(min(s1))
    del s1[:]
for z in range(0,len(ll1)):
    print(ll[z])
