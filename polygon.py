import sys

data = sys.stdin.read().split()

n = int(data[0])

g = data[2:] + data[1:]

ans = -float('inf')

mx = [[ans] * (4 * n) for _ in range(4 * n)]
mn = [[-ans] * (4 * n) for _ in range(4 * n)]

for i in range(2, 4*n-1, 2):
    mx[i][i] = int(g[i])
    mn[i][i] = int(g[i])

for length in range(0, 2*n, 2):
    for l in range(0, 4*n-length, 2):
        r = l + length
        for k in range(l, r, 2): 
               if g[k+1] == 'x':
                   mx[l][r] = max(mx[l][k] * mx[k+2][r],mn[l][k] *mx[k+2][r],
                                  mx[l][k] * mn[k+2][r],mn[l][k] * mn[k+2][r],
                                  mx[l][r])
                   mn[l][r] = min(mx[l][k] * mx[k+2][r],mn[l][k] *mx[k+2][r],
                                  mx[l][k] * mn[k+2][r],mn[l][k] * mn[k+2][r],
                                  mn[l][r])
               else:
                   mx[l][r] = max(mx[l][k] + mx[k+2][r],
                                  mx[l][r])
                   mn[l][r] = min(mn[l][k] + mn[k+2][r],
                                  mn[l][r])
                   
for l in range(0, 2*n, 2):
    r = l + 2 * n - 2
    ans = max (ans, mx[l][r])

edge = [] 
for l in range(0, 2*n, 2):
    r = l + 2 * n - 2
    if mx[l][r] == ans:
        d = (l // 2) % n + 1
        edge.append(d)
        
edge.sort()
    
print(int(ans))
print(*edge)