import sys
input = sys.stdin.readline
import heapq

out = []

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    start = int(input().strip(), 2)
    
    full = (1 << n) - 1
    
    act = []
    
    for row in range(m):
        d = int(input())
        g = int(input().strip(), 2)
        b = int(input().strip(), 2)
        
        act.append((d, g, b))
        
    time = [float('inf')] * ((1 << 10) + 5)
    time[start] = 0
    pq = [(0,start)]

    while pq:
        d, u = heapq.heappop(pq)
        
        if d != time[u]:
            continue
        
        for s, g, b in act:
            v = u & (full ^ g)
            v |= b
            
            if time[v] > d + s:
                time[v] = d + s
                
                heapq.heappush(pq, (time[v], v))
                
    if time[0] != float('inf'):
        out.append(str(time[0]))
    else:
        out.append(str(-1))
        
sys.stdout.write('\n'.join(out))