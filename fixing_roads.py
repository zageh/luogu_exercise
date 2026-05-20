import sys

data = sys.stdin.read().split()

n = int(data[0])
m = int(data[1])

p = [0] * (n + 1)
for i in range(1, n + 1):
    p[i] = i
    
roads = []

def find(x):
    if p[x] != p[p[x]]:
        p[x] =  find(p[x])
        
    return p[x]

def union(x, y):
    if find(x) != find(y):
        p[find(x)] = find(p[y])
        return False
    
    return True

idx = 2
for _ in range(m):
    x = int(data[idx])
    y = int(data[idx + 1])
    t = int(data[idx + 2])
    
    idx += 3
    
    roads.append((t,x,y))
    
roads.sort(key = lambda x: x[0])

cnt = n
for t, u, v in roads:
    if union(u, v):
        continue
    
    cnt -= 1
    
    if cnt == 1:
        print(t)
        sys.exit()
            
print(-1)