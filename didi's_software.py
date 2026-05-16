import sys
from collections import deque

data = sys.stdin.read().split()

n = int(data[0])
m = int(data[1])
q = int(data[2])
g = [[] for _ in range(n + 1)]

ans = []

idx = 3
for _ in range(m):
    u = int(data[idx])
    v = int(data[idx+1])
    
    idx +=2
    
    g[u].append(v)
    g[v].append(u)
    
vis = [(-1, -1)] * (n + 1)
cir = [False] * (n + 1)

dq = deque()

for i in range(1, n + 1):
    if vis[i][0] > -1:
        continue
    if not g[i]:
        continue
    
    vis[i] = (0, i)
    dq.append(i)
    
    while dq:
        u = dq.popleft()
        s, p = vis[u]
        
        for v in g[u]:
            if vis[v][0] > -1: 
                if vis[v][0] == s:
                    cir[p] = True
                continue
                
            vis[v] = (s ^ 1, p)
            dq.append(v)
            
for _ in range(q):
    s = int(data[idx])
    t = int(data[idx + 1])
    x = int(data[idx + 2])
    
    idx += 3
    
    ss, ps = vis[s]
    st, pt = vis[t]
    
    if s == t and x == 0:
        ans.append('tribool')
        continue
    
    if ps == -1 or pt == -1:
        ans.append('expand')
        continue
    
    if ps != pt:
        ans.append('expand')
        continue
    
    if cir[pt]:
        ans.append('tribool')
        continue
    
    check = x % 2
    
    if ss ^ check == st:
        ans.append('tribool')
    else:
        ans.append('expand')
        
sys.stdout.write('\n'.join(ans))