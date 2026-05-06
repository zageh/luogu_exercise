import sys
input = sys.stdin.readline

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    a = list(map(int,input().split()))
    
    ans = n
    suf = 0
    for i in range(n-1,-1,-1):
        if a[i] + suf <= 0:
            ans -= 1
        suf= max(suf + a[i], 0)
        
    print(ans)