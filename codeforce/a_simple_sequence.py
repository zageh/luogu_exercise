import sys
input=sys.stdin.readline

t=int(input().strip())
for _ in range(t):
    n=int(input().strip())
    
    ans=range(n,0,-1)
    print(*ans)