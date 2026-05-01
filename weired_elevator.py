import sys
from collections import deque
input=sys.stdin.readline

n,a,b=map(int,input().strip().split())
k=[0]+list(map(int,input().strip().split()))

q=deque([a])
step=[-1]*(n+1)
step[a]=0

if a==b:
    print(0)
    sys.exit()

while q:
    x=q.popleft()
    for i in (x-k[x],x+k[x]):
        if 1<=i<=n and step[i]==-1:
            step[i]=step[x]+1
            q.append(i)
            if i==b:
                print(step[i])
                sys.exit()

print(-1)