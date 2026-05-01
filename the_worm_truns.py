import sys
from collections import deque

data=sys.stdin.read().split()
idx=0
while True:
    n=int(data[idx])
    if n==0:
        break
    d=data[idx+1]
    dq=deque()

    ok=True
    vis=[[False]*51 for _ in range(51)]
    for i in range(11,31):
        vis[25][i]=True
        dq.append((25,i))
        
    for i in range(n):
        lx,ly=dq.popleft()
        vis[lx][ly]=False
            
        cx,cy=dq[-1]
        if d[i]=='E':
            nx,ny=cx,cy+1
        if d[i]=="W":
            nx,ny=cx,cy-1
        if d[i]=="N":
            nx,ny=cx-1,cy
        if d[i]=="S":
            nx,ny=cx+1,cy
        if nx>50 or nx<1 or ny>50 or ny<1:
            print(f"The worm ran off the board on move {i+1}.")
            ok=False
            break
        if vis[nx][ny]:
            print(f"The worm ran into itself on move {i+1}.")
            ok=False
            break
        
        vis[nx][ny]=True
        dq.append((nx,ny))
    
    if ok:    
        print(f"The worm successfully made all {n} moves.")
    idx+=2