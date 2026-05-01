import sys
from collections import deque
input=sys.stdin.readline

m=int(input().strip())
ranch=[[10**7]*(305) for _ in range(305)]
danger=[[10**7]*(305) for _ in range(305)]
ranch[0][0]=0

mx=(0,0,-1,1)
my=(1,-1,0,0)

for _ in range(m):
    x,y,t=map(int,input().strip().split())
    
    if x==0 and y==0 and t==0:
        print(-1)
        sys.exit()
        
    danger[x][y]=min(t,danger[x][y])
    for i in range(4):
        nx=x+mx[i]
        ny=y+my[i]
        if 0<=nx<=305 and 0<=ny<=305:
            danger[nx][ny]=min(danger[nx][ny],t)

if danger[0][0]==10**7:
    print(0)
    sys.exit()

q=deque([(0,0)])
while q:
    x=q.popleft()
    cx,cy=x[0],x[1]
    for i in range(4):
        nx=cx+mx[i]
        ny=cy+my[i]

        if 0<=nx<=305 and 0<=ny<=305 and ranch[cx][cy]+1<danger[nx][ny]:
            if ranch[nx][ny]==10**7:
                ranch[nx][ny]=ranch[cx][cy]+1
                q.append((nx,ny))
            if danger[nx][ny]==10**7:
                print(ranch[nx][ny])
                sys.exit()

print(-1)