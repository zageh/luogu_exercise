import sys
input=sys.stdin.readline

t=int(input().strip())
for _ in range(t):
    s,m=map(int,input().split())
    if s&m!=s:
        print(-1)
    else:
        ans=s//m
        if s%m!=0:
            ans+=1
        print(ans)