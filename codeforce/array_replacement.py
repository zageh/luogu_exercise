import sys
input=sys.stdin.readline

t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    
    d = [0] * (n - 1)
    for i in range(n - 1):
        d[i] = a[i + 1] - a[i]
        
    l = 0
    while l < n - 1:
        r = l + 1
        
        while r < n - 1 and d[r] % 2 == d[l] % 2:
            r += 1
            
        d[l:r] = sorted(d[l: r])
        l = r
        
    out = [a[0]]
    ans = a[0]
    for x in d:
        ans += x
        out.append(ans)
        
    print(*out)