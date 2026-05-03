import sys
input=sys.stdin.readline
from collections import Counter

mod=998244353
M=200005

fac=[1]*(M+1)
inv=[1]*(M+1)
for i in range(2, M + 1):
    fac[i] = fac[i-1] * i % mod
inv[M] = pow (fac[M], mod - 2, mod)
for i in range(M, 0, -1):
    inv[i-1] = inv[i] * i % mod 
    
def p(i, j):
    if j <0 or j > i:
        return 0
    
    return fac[i] * inv[i - j] % mod

out = []

t=int(input().strip())
for _ in range(t):
    n=int(input().strip())
    pre=list(map(int,input().split()))
    
    cnt=Counter(pre)
      
    ans=1
    
    l=n  
    for k,v in cnt.items():
        if l < k:
            ans = 0
            break
        
        ans = (ans * p(l - k, v - 1)) % mod
        
        l -= v
        
    out.append(str(ans))
    
print('\n'.join(out))