from collections import deque
import sys
input=sys.stdin.readline

mod=80112002

n,m=map(int,input().strip().split())
pred=[[] for _ in range(n+1)]
dp=[0]*(n+1)
indeg=[0]*(n+1)
outdeg=[0]*(n+1)

for _ in range(m):
    e,p=map(int,input().strip().split())
    pred[e].append(p)
    indeg[p]+=1
    outdeg[e]+=1

q=deque()
for i in range(1,n+1):
    if indeg[i]==0:
        q.append(i)
        dp[i]=1

while q:
    e=q.popleft()
    for p in pred[e]:
        indeg[p]-=1
        dp[p]=(dp[p]+dp[e])%mod
        if indeg[p]==0:
            q.append(p)

ans=0
for i in range(1,n+1):
    if outdeg[i]==0:
        ans=(dp[i]+ans)%mod

print(ans)