import sys
input=sys.stdin.readline

t=int(input())
for _ in range(t):
    n = int(input())
    a = [0] + list(map(int, input().split()))
    
    ans = [a[1]]
    
    pre = a[1]
    
    if n == 1:
        print(pre)
        continue
    
    for i in range(2, n + 1):
        pre += a[i]
        
        avg = pre // i
        
        ans.append(min(ans[-1], avg))
        
    print(*ans)