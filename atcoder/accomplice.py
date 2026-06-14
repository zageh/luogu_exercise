import sys
import math

data = sys.stdin.read().split()

n = int(data[0])
d = int(data[1])
left = [0] * (10 ** 6 + 5)
right = [0] * (10 ** 6 + 5)

idx = 2
for i in range(n):
    s = int(data[idx])
    e = int(data[idx + 1])
    
    l = s
    r = e - d
    
    if l <= r:
        left[l] += 1
        right[r + 1] += 1
    
    idx += 2

cur = 0 
ans = 0   
for t in range(1, 10 ** 6 + 1):
    cur += left[t]
    cur -= right[t]
    
    ans += math.comb(cur, 2)
    
print(ans)