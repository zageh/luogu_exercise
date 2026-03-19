import sys
input = sys.stdin.readline

length,n,k=map(int,input().strip().split())
pos=list(map(int,input().strip().split()))

dis=[]
last=0
for p in pos:
    dis.append(p-last)
    last=p
dis.append(length-pos[-1])
    
def check(m:int):
    num=k
    for d in dis:
        if d/num>m:
            return False
        for i in range(2,num):
            if d/i<=m:
                num-=i
                break
    return True

l=min(dis)
r=max(dis)
while l<r:
    mid=(l+r)//2
    if check(mid):
        r=mid
    else:
        l=mid+1

print(l)
            
