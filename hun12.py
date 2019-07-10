aa3,bb3=map(int,input().split())
ls=list(map(int,input().split()))
l2=[]
for i in range(0,bb3):
     uu3,vv3=map(int,input().split())
     l2.append([uu3,vv3])
for i in range(bb3):
     lower=l2[i][0]
     upper=l2[i][1]
     ss3=sum(ls[lower-1:upper])
     print(ss3)
