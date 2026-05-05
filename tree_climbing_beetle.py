import sys

data = sys.stdin.read().split()

mod = 998244353

n = int(data[0])

idx = 1
p = []
for _ in range(n):
    x = int(data[idx])
    y = int(data[idx+1])
    
    p.append((x,y))
    
    idx += 2
    
pre = [0] * (n + 1)
pre[0] = 1
mulx = [1] * (n + 1)
muly = [1] * (n + 1)

for i in range(1,n+1):
    mulx[i] = (mulx[i-1] * (p[i-1][1] - p[i-1][0])) % mod
    muly[i] = (muly[i-1] * p[i-1][1]) % mod
    pre[i] = (pre[i-1] + mulx[i] * pow(muly[i], mod-2, mod)) % mod 
    
ans = (pre[n-1] * muly[n] %mod * pow(mulx[n], mod-2, mod)) % mod
print(ans)