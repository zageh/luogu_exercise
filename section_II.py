import sys
input = sys.stdin.readline

n,m=map(int,input().strip().split())
a=list(map(int,input().strip().split()))

def check(x:int):
    cur=0
    cnt=1
    for num in a:
        if cur+num<=x:
            cur+=num
        else:
            cur=num
            cnt+=1

    return cnt<=m

l,r=max(a),sum(a)
while l<r:
    mid=(l+r)//2
    if check(mid):
        r=mid
    else:
        l=mid+1

print(l)
