import sys
input=sys.stdin.readline
from collections import deque

n=int(input().strip())
g=[[] for _ in range(n+1)]

for i in range(n-1):
    u,v=map(int,input().split())
    g[u].append(v)
    g[v].append(u)

def bfs(start):
    dist=[-1]*(n+1)
    dist[start]=0
    q=deque([start])
    far=start

    while q:
        u=q.popleft()
        for v in g[u]:
            if dist[v]==-1:
                dist[v]=dist[u]+1
                q.append(v)
                if dist[v]>dist[far]:
                    far=v

    return far,dist[far]

u,_=bfs(1)
v,d=bfs(u)

print(d-d%2)