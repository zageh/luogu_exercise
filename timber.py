import sys
input=sys.stdin.readline

n,s,le=map(int,input().split())
h=list(map(int,input().split()))
a=list(map(int,input().split()))
    
def check(w:int):
    global s
    
    cnt=0
    for i in range(n):
        if h[i]+a[i]*w>=le:
            cnt+=h[i]+a[i]*w
    
    return cnt>=s

if not check(0) and max(a)==0:
    print(-1)
    sys.exit()

l,r=0,1
wait=True
while wait:
    if not check(r):
        l=r
        r*=2
    else:
        while l<r:
            mid=(l+r)//2
            if check(mid):
                r=mid
            else:
                l=mid+1
        wait=False
        
print(r)