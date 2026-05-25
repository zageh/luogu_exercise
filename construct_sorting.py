import sys
from collections import Counter

data = sys.stdin.read().split()

n = int(data[0])
a = [int(x) for x in data[1:]]

cnt = Counter(a)

for x in cnt.values():
    if x > 2:
        print(-1)
        sys.exit()
  
plus = []
x = 1
while x < n + 1:
    if cnt[x] == 0:
        plus.append(x)
        
    x += 1

b = a[:]
ib = 0
c = a[:]
ic = 0
 
vis = [False] * (n + 1)       
for i in range(n):
    if a[i] < 1 or a[i] > n:
        print(-1)
        sys.exit()
        
    if cnt[a[i]] == 2:
        if vis[a[i]]:
            b[i] = plus[ib]
            ib += 1
        else:
            c[i] = plus[ic]
            vis[a[i]] = True
            ic += 1 
            
print(*b)
print(*c)           