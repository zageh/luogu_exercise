import sys
import heapq

data=sys.stdin.read().split()
n=int(data[0])
m=int(data[1])
s=int(data[2])

adj=[[]  for _ in range(n+1)]

idx=3
for _ in range(m):
    u=int(data[idx])
    v=int(data[idx+1])
    w=int(data[idx+2])
    adj[u].append((v,w))
    idx+=3

dist=[float('inf')]*(n+1)
dist[s]=0
pq=[(0,s)]

while pq:
    d,u=heapq.heappop(pq)

    if d>dist[u]:
        continue

    for e,l in adj[u]:
        if dist[e]>l+dist[u]:
            dist[e]=l+dist[u]
            heapq.heappush(pq,(dist[e],e))

result=[str(dist[i]) for i in range(1,n+1)]
print(' '.join(result))