import sys
input=sys.stdin.readline

from collections import Counter

t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    
    cnt = Counter(a)
    
    tot = 0
    mx = 0
    for k, v in cnt.items():
        if 2 * v > n + 1:
            mx = k
            tot += (2 + n - v) * k
            
    for k, v in cnt.items():
        if k == mx:
            continue
        
        tot += k * v
        
    print(tot)