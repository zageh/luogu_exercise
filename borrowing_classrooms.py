import sys
from array import array#太吊了这个，夯
input=sys.stdin.readline

n,m=map(int,input().split())
r=list(map(int,input().split()))
d=array('I',[0])*m
s=array('I',[0])*m
t=array('I',[0])*m  
diff=[0]*(n+1)

for i in range(m):
    d[i],s[i],t[i]=map(int,input().split())
    s[i]-=1
    t[i]-=1

def check(x:int)->bool:
    for i in range(n+1):
        diff[i]=0
    for i in range(x):
        diff[s[i]]+=d[i]
        if t[i]+1<n:
            diff[t[i]+1]-=d[i]

    cur=0
    for i in range(n):
        cur+=diff[i]
        if cur>r[i]:
            return False
    return True

if check(m):
    print(0)
    sys.exit()

l,ri=1,m
ans=0
while l<=ri:
    mid=(l+ri)//2
    if check(mid):
        l=mid+1
    else:
        ans=mid
        ri=mid-1
        
print(-1)
print(ans)