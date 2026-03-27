import sys
from collections import deque

mx=(1,1,1,-1,-1,-1,0,0)
my=(0,1,-1,0,-1,1,1,-1)

x,y,xm,ym=map(int,input().split())
ranch=[]
for _ in range(y):
    a=sys.stdin.readline
    ranch.append(a)

q=deque()
q.append((xm,ym))
ranch[ym][xm]='0'

ans=0
while q:
    cx,cy=q.popleft()
    
    for n in range(8):
        nx,ny=cx+mx[n],cy+my[n]
        
        if 0<=nx<x and 0<=ny<y and ranch[ny][nx]=='.':
            ranch[ny][nx]=ranch[cx][cy]+1
            ans=max(ans,ranch[ny][nx])
            q.append((nx,ny))
            
        else:
            continue
        
print(int(ans)-48)