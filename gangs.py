import sys

data = sys.stdin.read().split()

n = int(data[0])
m = int(data[1])
friend = []
enemy = []
e = [[] for _ in range(n + 1)]

idx = 2
for _ in range(m):
    r = data[idx]
    u = int(data[idx + 1])
    v = int(data[idx + 2])
    
    idx += 3
    
    if r == 'E':
        enemy.append((u,v))
        e[u].append(v)
        e[v].append(u)
    else:
        friend.append((u,v))
        
p = [0] * (n + 1)
for i in range(1, n + 1):
    p[i] = i

def find(x):
    while x != p[x]:
        p[x] = p[p[x]]
        x = p[x]
        
    return x

def union(x, y):
    fx = find(x)
    fy = find(y)
    
    if fx != fy:
        p[fx] = p[fy]
        
for u, v in enemy:
    for x in e[u]:
        union(x, v)
    for x in e[v]:
        union(x, u)  

for u, v in friend:
    union(u,v)
        
print(len(set(find(i) for i in range(1, n + 1))))