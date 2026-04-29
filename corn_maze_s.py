import sys
input=sys.stdin.readline
from collections import deque

m,n=map(int,input().strip().split())
maze=['']*(m+1)
steps=[[10**7]*(n+1) for _ in range(m+1)]
q=deque()
end=(-1,-1)

slip={}
sl={}

for i in range(m):
    maze[i]=input().strip()
    for j in range(n):
        if 'A'<=maze[i][j]<='Z':
            if maze[i][j] not in slip:
                slip[maze[i][j]]=(i,j)
            else:
                sl[maze[i][j]]=(i,j)
        if maze[i][j]=='=':
            end=(i,j)
        if maze[i][j]=='@':
            steps[i][j]=0
            q.append((i,j))

if end==(-1,-1):
    print(-1)
    sys.exit()

mx=(1,-1,0,0)
my=(0,0,1,-1)

while q:
    cur=q.popleft()

    cx,cy=cur

    for i in range(4):
        nx=cx+mx[i]
        ny=cy+my[i]

        if nx>=m or nx<0 or ny>=n or ny<0:
            continue

        if maze[nx][ny]=='#':
            continue

        if 'A'<=maze[nx][ny]<='Z':
            if slip[maze[nx][ny]]==(nx,ny):
                tx,ty=sl[maze[nx][ny]] 
            else:
                tx,ty=slip[maze[nx][ny]]
                
            if steps[tx][ty]>steps[cx][cy] + 1:
                steps[tx][ty]=steps[cx][cy] + 1
                q.append((tx, ty))

        else:
            if steps[nx][ny]>steps[cx][cy] + 1:
                steps[nx][ny]=steps[cx][cy] + 1
                q.append((nx, ny)) 

ex,ey=end
print(steps[ex][ey])