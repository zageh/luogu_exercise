import sys
input=sys.stdin.readline

leng,n,m=map(int,input().strip().split())
pos=[0]+[int(input().strip()) for _ in range(n)]+[leng]
    
def check(x:int):
    last=0
    used=0
    for i in range(1,n+2):
        if pos[i]-pos[last]<x:
            used+=1
        else:
            last=i
            
            
    return used<=m

l,r=1,leng
while l<r:
    mid=(l+r+1)//2
    if check(mid):
        l=mid
    else:
        r=mid-1
        
print(l)        