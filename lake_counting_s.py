import sys
input=sys.stdin.readline
from collections import deque

mx=(1,-1,0,0,1,1,-1,-1)
my=(0,0,1,-1,1,-1,1,-1)

n,m=map(int,input().split())
field=['0']*m
for i in range(n):
    s=input().strip()
    field[i]=s

vis=[[False]*m for _ in range(n)]
cnt=0

for i in range(n):
    for j in range(m):
        if field[i][j]=='W' and not vis[i][j]:
            cnt+=1
            vis[i][j]=True
            q=deque()
            q.append((i,j))

            while q:
                cur=q.popleft()
                cx,cy=cur

                for d in range(8):
                    nx,ny=cx+mx[d],cy+my[d]

                    if 0<=nx<n and 0<=ny<m and field[nx][ny]=='W' and not vis[nx][ny]:
                        q.append((nx,ny))
                        vis[nx][ny]=True
                    else:
                        continue

print(cnt)