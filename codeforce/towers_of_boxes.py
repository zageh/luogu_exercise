import sys
input=sys.stdin.readline

t=int(input().strip())
for _ in range(t):
    n,m,d=map(int,input().split())
    per=1+d//m
    ans=n//per
    t=n%per
    if t!=0:
        ans+=1
        
    print(ans)