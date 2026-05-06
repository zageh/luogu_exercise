import sys
input = sys.stdin.readline

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    a = list(map(int,input().split()))
    
    s = set(a)
    if s == {0}:
        print(n)
        continue
    
    mx = 0
    while mx in s:
        mx += 1
    
    p = max(a)
    
    if p == mx - 1:
        ans = p * n + (mx - 1) * (mx - 2) // 2 + (n + 1 - mx) * mx
    else:
        ans = p * n + (mx + 1) * mx // 2 + (n - 1 - mx) * mx
        
    print(ans)