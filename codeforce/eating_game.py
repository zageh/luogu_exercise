import sys
input=sys.stdin.readline

t=int(input().strip())
for _ in range(t):
    n=int(input().strip())
    a=list(map(int,input().split()))
    m=max(a)
    ans=a.count(m)
    print(ans)