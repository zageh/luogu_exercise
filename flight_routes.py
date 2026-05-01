import sys
input=sys.stdin.readline
import heapq

n,m,k=map(int,input().split())
s,t=map(int,input().split())

dist=[[float('inf')]*(k+1) for _ in range(n+1)]
for i in range(k):
    dist[s][i]=0

g=[[]for _ in range(n+1)]
for _ in range(m):
    a,b,c=map(int,input().split())
    g[a].append((b,c))
    g[b].append((a,c))

pq=[(0,s,0)]

while pq:
    d,u,i=heapq.heappop(pq)
    if d>dist[u][i]:
        continue

    for v,c in g[u]:
        if dist[v][i]>d+c:
            dist[v][i]=d+c
            heapq.heappush(pq,(dist[v][i],v,i))

        if i<k:
            if dist[v][i+1]>d:
                dist[v][i+1]=d
                heapq.heappush(pq,(dist[v][i+1],v,i+1))

print(min(dist[t]))