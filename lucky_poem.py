import sys
input=sys.stdin.readline

n,x=map(int,input().split())
a=list(map(int,input().split()))

cur=sum(a)
pre=0
best=0
mn=0
for y in a:
    pre+=x-y
    best=max(best,pre-mn)
    mn=min(mn,pre)

ans=cur+best
print(ans)