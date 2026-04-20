import sys
input=sys.stdin.readline

def min_range(n,k,a):
    a.sort()
    ans=float('inf')

    if k>=n-1:
        return 0
    
    for c in range(k//3+1):
        remove=k-c
        
        d1,d2=c,remove-c
        l1,r1=d1,n-d2-1
        if r1>=l1:
            ans=min(ans,a[r1]-a[l1])

        l2,r2=d2,n-d1-1
        if r2>=l2:
            ans=min(ans,a[r2]-a[l2])

    return ans

t=int(input().strip())

for _ in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))

    ans=min_range(n,k,a)

    print(ans)