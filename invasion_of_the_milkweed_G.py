import sys
from collections import deque

mx=(1,1,1,-1,-1,-1,0,0)
my=(0,1,-1,0,-1,1,1,-1)

x,y,xm,ym=map(int,input().split())
ranch=[list(sys.stdin.readline().strip()) for _ in range(y)]

q=deque()
q.append((xm-1,y-ym))
ranch[y-ym][xm-1]='0'

ans='0'
while q:
    cx,cy=q.popleft()
    
    for n in range(8):
        nx,ny=cx+mx[n],cy+my[n]
        
        if 0<=nx<x and 0<=ny<y and ranch[ny][nx]=='.':
            ranch[ny][nx]=chr(ord(ranch[cy][cx])+1)
            ans=max(ans,ranch[ny][nx])
            q.append((nx,ny))
            
        else:
            continue
        
print(ord(ans)-ord('0'))