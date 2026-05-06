import sys
from collections import deque

data = sys.stdin.read().split()

n = int(data[0])
m = int(data[1])
p = [0] + [int(x) for x in data[2:]]
ans = -10**18

pre = [0] * (n + 1)

for i in range(1, n+1):
    pre[i] = pre[i-1] + p[i]
   
pq = deque() 

pq.append(0)
for i in range(1, n+1):
    while pq and pq[0] + m < i:
        pq.popleft()
        
    ans = max(ans, pre[i] - pre[pq[0]])
    
    while pq and pre[pq[-1]] > pre[i]:
        pq.pop()
        
    pq.append(i)
        
    
    
print(ans)