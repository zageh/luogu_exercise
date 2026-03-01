import sys
input=sys.stdin.readline

n,m=map(int,input().split())
lst=[]
for i in range(m):
    p,a=map(int,input().split())
    lst.append((p,a))

lst.sort(key=lambda x:x[0])
cnt=n
cost=0
while cnt>0:
    for p,a in lst:
        if cnt<a:
            cost+=cnt*p
            cnt=0
        else:
            cost+=a*p
            cnt-=a

print(cost)