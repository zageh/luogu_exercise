import sys
input=sys.stdin.readline

dirs=[(0,1),(1,0),(0,0),(-1,0),(0,-1)]

a=[list(map(int,input().strip().split())) for _ in range(3)]

ans=10**20

for mask in range(1<<9):
    b=[row[:] for row in a]
    cnt=0
    
    for k in range(9):
        if (mask>>k)&1:
            cnt+=1
            x,y=divmod(k,3)

            for mx,my in dirs:
                nx,ny=x+mx,y+my
    
                if 2>=nx>=0 and 0<=ny<=2:
                    b[nx][ny]^=1

    ok=True
    for i in range(3):
        for j in range(3):
            if b[i][j]==0:
                ok=False
                break

        if not ok:
            break

    if ok:
        ans=min(ans,cnt)

print(ans)