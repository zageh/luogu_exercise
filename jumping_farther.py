import sys

data=sys.stdin.read().split()

n=int(data[0])
m=int(data[1])
a=[0]+[int(x) for x in data[2:]]
dis=[0]*(n+1)
for i in range(1,n+1):
    dis[i]=a[i]-a[i-1]

md=max(dis)
def check(l:int):
    global m,md

    cnt=0
    used=False
    for d in dis:
        if d==md and not used:
            if md<2*l:
                used=True
                continue
            else:
                d=md-2*l
                used=True
                cnt+=1

        if d<=l:
            continue
                
        n=d//l
        if d%l!=0:
            n+=1
        cnt+=n-1
        if cnt>m:
            return False

    return cnt<=m

left,r=1,md
while left<r:
    mid=(left+r)//2
    if check(mid):
        r=mid
    else:
        left=mid+1

print(r)