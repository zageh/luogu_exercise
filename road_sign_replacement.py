import sys
input = sys.stdin.readline

length,n,k=map(int,input().strip().split())
pos=list(map(int,input().strip().split()))

dis=[]
for i in range(1,n):
    dis.append(pos[i]-pos[i-1])
    
def check(m:int):
    used=0
    for d in dis:
        used+=(d-1)//m
        if used>k:
            return False
    return True

l=1
r=max(dis)
while l<r:
    mid=(l+r)//2
    if check(mid):
        r=mid
    else:
        l=mid+1

print(l)
            
