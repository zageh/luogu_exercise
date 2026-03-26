import sys
input=sys.stdin.buffer.readline
from collections import deque

n,m=map(int,input().split())

big=[0]*(n+1)
p=[[] for _ in range(n+1)]
ans=[0]*(n+1)

for _ in range(m):
    s,e=map(int,input().split())
    p[e].append(s)
    
for i in range(n,0,-1):
    if big[i]==0:
        stack=[i]
        big[i]=i
    
        while stack:
            x=stack.pop()

            for y in p[x]:
                if big[y]==0:
                    stack.append(y)
                    big[y]=i
    
print(*big[1:])
