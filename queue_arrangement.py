import sys
input=sys.stdin.readline

n=int(input().strip())
lst=[]
pos=[[0,0] for _ in range(n+1)]

for i in range(2,n+1):
    x,r=map(int,input().strip().split())
    if pos[x][r]==0:
        pos[x][r]=i
        pos[i][abs(r-1)]=x
    else:
        y=pos[x][r]
        pos[x][r]=i
        pos[y][abs(r-1)]=i
        pos[i][r]=y
        pos[i][abs(r-1)]=x

inside=[True]*(n+1)

m=int(input().strip())
for _ in range(m):
    x=int(input().strip())
    if inside[x]:
        r=pos[x][1]
        l=pos[x][0]
        if l:
            pos[l][1]=r
        if r:
            pos[r][0]=l
        inside[x]=False

cur=0
for i in range(1,n+1):
    if pos[i][0]==0 and inside[i]:
        cur=i
        break

ans=[]
while cur:
    ans.append(cur)
    cur=pos[cur][1]

print(*ans)