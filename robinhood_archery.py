import sys
input = sys.stdin.readline
import time
import random

random.seed(time.time_ns())

mp = {}

def p(x):
    if x not in mp:
        mp[x] = (random.getrandbits(64), random.getrandbits(64))
    return mp[x]

out = []
t = int(input())
for _ in range(t):
    n, q=map(int,input().split())
    a = [0] + list(map(int,input().split()))
        
    pre1 = [0] * (n + 1)
    pre2 = [0] * (n + 1)
    
    for i in range(1, n + 1):
        h1, h2 =p(a[i])
        pre1[i] = pre1[i - 1] ^ h1
        pre2[i] = pre2[i - 1] ^ h2
        
    ans = []
    for i in range(q):
        l, r = map(int,input().split())
        
        j1 = pre1[l - 1] ^ pre1[r]
        j2 = pre2[l - 1] ^ pre2[r]
        
        if j1 == 0 and j2 == 0:
            ans.append('YES') 
        else:
            ans.append('NO')
            
    out.extend(ans)
            
sys.stdout.write('\n'.join(out))