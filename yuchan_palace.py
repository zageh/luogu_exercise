import sys

data = sys.stdin.read().split()

n = int(data[0])
m = int(data[1])

graph = []
idx = 2
for _ in range(n):
    graph.append(data[idx:idx+m])
    
    idx += m
    
ans = 0

up = [0] * (m+1)
left = [0] * (m+1)
right = [m] * (m+1)

for i in range(n):
    cur_l = 0
    cur_r = m
    
    for j in range(m):
        if graph[i][j] == 'F':
            up[j] += 1
            left[j] = max(cur_l, left[j])
        else:
            up[j] = 0
            left[j] = 0
            cur_l = j + 1
            
    for j in range(m-1, -1, -1):
        if graph[i][j] == 'F':
            right[j] = min(right[j], cur_r)
        else:
            right[j] = m
            cur_r = j
            
    for j in range(m):
        if graph[i][j] == 'F':
            cand = up[j] * (right[j] - left[j])
            if cand > ans:
                ans = cand
     
ans *=3   
print(ans)