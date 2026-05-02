import sys

data = sys.stdin.read().split()

mod = 1000000007

n = int(data[0])

fac = [1] * (n+1)
for i in range(1,n+1):
    fac[i] = fac[i-1] * i % mod
    
inv=[1] * (n+1)
inv[n] = pow(fac[n], mod - 2, mod)
for i in range(n, 0, -1):
    inv[i-1] = inv[i] * i % mod
    
def c(a, b):
    if b < 0 or b > a:
        return 0
    return fac[a] * inv[b] % mod * inv[a - b] % mod

v = [0] * (n+1)

idx = 1
for _ in range(n-1):
    s = int(data[idx])
    t = int(data[idx+1])
    
    v[s] += 1
    v[t] += 1
    
    idx += 2
        
l = int(data[-2])
r = int(data[-1])

cnt = [0]*(n+1)

for i in range(1,n+1):
    cnt[v[i]] += 1

ans = 0
if l <= 1 <= r:
    ans +=n           
if l <= 2 <= r:
    ans += n-1
 
for i in range(2,n+1):
    if cnt[i] == 0:
        continue
    
    for j in range(max(2,l-1),min(r-1,i)+1):
        ans = (ans + c(i,j) * cnt[i]) % mod 
    
print(ans % mod)