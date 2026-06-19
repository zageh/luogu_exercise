import sys
input = sys.stdin.readline

from bisect import bisect_left

out = []

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    used = [False] * n
    
    c = a[:]
    
    c.sort()
    
    for i in range(n):
        if c[i] > b[i]:
            out.append('-1')
            n = 0
            break
        
    if not n:
        continue
    
    p = []
    cnt = 0
    for i in range(n):
        j = bisect_left(b, a[i])
            
        while j < n and used[j]:
            j += 1
                
        if j == n:
            n = 0
            break
                
        used[j] = True
        p.append(j)
            
    if not n:
        out.append('-1')
        continue
    
    for i in range(n):
        for j in range(i + 1, n):
            if p[i] > p[j]:
                cnt += 1
            
    out.append(str(cnt))
    
sys.stdout.write('\n'.join(out))