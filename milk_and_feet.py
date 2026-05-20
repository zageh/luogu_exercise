import sys
from collections import deque

data = sys.stdin.read().split()

n = int(data[0])
a = [0] + [int(x) for x in data[1:]]

mn = [0] * (n + 1)
pre = [0] * (n + 1)

dq = deque()
dq.append(1)

mn[1] = a[1]

for i in range(2, n + 1):
    cur = a[i]
    
    while dq and a[dq[-1]] >= cur:
        dq.pop()
       
    if dq:
        p = dq[-1]
        pre[i] = p
    else:
        pre[i] = 0
        
    dq.append(i)
    
dq.clear()

for i in range(n, 0, -1):
    cur = a[i]
    
    while dq and a[dq[-1]] >= cur:
        dq.pop()
        
    if dq:
        p = dq[-1]
        l = p - pre[i] - 1
    else:
        l = n - pre[i]
        
    if a[i] > mn[l]:
        mn[l] = a[i]
        
    dq.append(i)
    
for i in range(n - 1, 0, -1):
    if mn[i] < mn[i + 1]:
        mn[i] = mn[i + 1]
        
sys.stdout.write(' '.join(map(str,mn[1:]))) 