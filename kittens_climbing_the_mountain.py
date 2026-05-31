import sys

data = sys.stdin.read().split()

n = int(data[0])
w = int(data[1])
c = [int(x) for x in data[2:]]

c.sort(reverse = True)
if c[-1] > w:
    print(-1)
    sys.exit()
    
wei = [0] * 20
ans = n
def dfs(u, v):
    global ans
    
    if v >= ans:
        return
    
    if u == n:
        ans = v
        return
    
    for i in range(1, v + 1):
        if wei[i] + c[u] <= w:
            wei[i] += c[u]
            dfs(u + 1, v)
            wei[i] -= c[u]
            
    wei[v + 1] = c[u]
    dfs(u + 1, v + 1)
    wei[v + 1] = 0
    
dfs(0, 0)

print(ans)