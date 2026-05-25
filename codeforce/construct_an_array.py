import sys
input=sys.stdin.readline

t=int(input().strip())
for _ in range(t):
    n=int(input().strip())
    
    ans = [x for x in range(2 * n - 1, n - 1, -1)]
    
    print(*ans)