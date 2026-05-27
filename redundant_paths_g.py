import sys

data = sys.stdin.read().split()

f = int(data[0])
r = int(data[1])
g = [[] for _ in range(f + 1)]

timer = 0
low = [0] * (f + 1)
dfn = [0] * (f + 1)

idx = 2
for i in range(1, r + 1):
    u = int(data[idx])
    v = int(data[idx + 1])
    
    idx += 2
    
    g[u].append((v, i))
    g[v].append((u, i))
    
bridge = [False] * (r + 1)
def tarjan(u, idx):
    global timer
    timer += 1
    low[u] = dfn[u] = timer
    
    for v, i in g[u]:
        if i == idx:
            continue
        
        if not dfn[v]:
            tarjan(v, i)
            
            low[u] = min(low[u], low[v])
            
            if low[v] >= dfn[u]:
                bridge[i] = True
                 
        else:
            low[u] = min(low[u], dfn[v])
            
for i in range(1, f + 1):
    if not dfn[i]:
        tarjan(i, -1)
      
bel = [0] * (f + 1)
def paint(u, col):
    bel[u] = col
    
    for v, idx in g[u]:
        if bridge[idx]:
            continue
        
        if not bel[v]:
            paint(v, col)

col = 0          
for i in range(1, f + 1):
    if not bel[i]:
        col += 1
        paint(i, col)
        
deg = [0] * (col + 1)

for u in range(1, f + 1):
    for v, idx in g[u]:
        if bridge[idx] and bel[u] != bel[v]:
            deg[bel[u]] += 1

leaf = 0         
for c in range(1, col + 1):
    if deg[c] == 1:
        leaf += 1
        
print((leaf + 1) >> 1)