import sys

data = sys.stdin.read().split()

n = int(data[0])
p = []

idx = 1
for _ in range(n):
    x = int(data[idx])
    y = int(data[idx + 1])
    
    p.append((x, y))
    
    idx += 2
    
p.sort()

mn = 1e6
cnt = 0

for x, y in p:
    if y < mn:
        cnt += 1
        mn = y
        
print(cnt)