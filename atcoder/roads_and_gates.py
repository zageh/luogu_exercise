import sys
import heapq

data = sys.stdin.read().split()

n, m, z = map(int, data[:3])

g = [[]for _ in range(n + 1)]

idx = 3
for _ in range(m):
    x, y, t = map(int, data[idx: idx+3])
    
    g[x].append((y, t))
    g[y].append((x, t))
    
    idx += 3
    
x = [0] + [int(x) for x in data[idx:]]

for i in range(1, n + 1):
    g[i].append((0, x[i]))
    g[0].append((i, x[i] + z))

inf = 10 ** 30
dis = [inf] * (n + 1)
dis[1] = 0

pq = [(0, 1)]

while pq:
    d, u = heapq.heappop(pq)
    
    if d != dis[u]:
        continue
    
    for v, t in g[u]:
        new = d + t
        
        if new < dis[v]:
            dis[v] = new
            heapq.heappush(pq, (new, v))
            
sys.stdout.write('\n'.join(map(str, dis[2:])))