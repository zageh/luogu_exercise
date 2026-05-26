import sys

data = sys.stdin.buffer.read().split()

n = int(data[0])
a = [int(x) for x in data[1: n + 1]]
b = [int(x) for x in data[n + 1:]]

total = sum(b)

maxa = 10 ** 6 + 10
cnt = [0] * maxa

best = b[0]

a0 = a[0]
b0 = b[0]

for k in range(10 ** 6 + 1):
    touched = []
    
    if k == 0:
        limit = n
    else:
        limit = min(n, maxa // k + 1)
        
    for i in range(1, limit):
        c = a[i] - k * i
        
        if c < 0:
            continue
        
        cnt[c] += b[i]
        touched.append(c)
        
        cur = cnt[c]
        
        if c == a0:
            cur += b0
        
        if cur > best:
            best = cur
            
    for c in touched:
        cnt[c] = 0
        
print(total - best)