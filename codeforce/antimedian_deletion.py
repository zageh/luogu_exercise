import sys
input=sys.stdin.readline

t=int(input().strip())
for _ in range(t):
    n=int(input().strip())
    p=list(map(int,input().split()))
    
    if n==1:
        ans=[1]
    else:
        ans=[2]*n
    
    print(*ans)