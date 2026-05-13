import sys
from collections import deque

data = sys.stdin.read().split()

n = int(data[0])
h = [float('inf')] + [int(x) for x in data[1:]]

w = [0] * (n + 1)
w[0] = 1

dq = deque()
dq.append(0)

for i in range(1, n+1):
    while dq and h[dq[-1]] < h[i]:
        dq.pop()
        
    w[i] = h[i] * (i - dq[-1]) + w[dq[-1]]
    
    dq.append(i)
    
print(*w[1:])