import sys

data = sys.stdin.read().split()

mod = 10007

n = int(data[0])
m = int(data[1])
v = [0] + [int(x) for x in data[2: 2+n]]
c = [0] + [int(x) for x in data[2+n: 2+2*n]]

cnt = [[0] * 2 for _ in range(m+1)]
s = [[0] * 2 for _ in range(m+1)]

for i in range(1, n+1):
    d = i % 2
    cnt[c[i]][d] += 1
    s[c[i]][d] += v[i]
    
ans = 0

for i in range(1, n+1):
    col = c[i]
    d = i % 2
    l = cnt[col][d]
    
    ans = (ans + i * (v[i] * (l - 2) + s[col][d])) % mod
                
print(ans)