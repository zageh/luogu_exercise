import sys
input=sys.stdin.readline
import math

mod=676767677

def cnt(x:int)->int:
    if x==0:
        return 1
    
    n=int(math.sqrt(x))
    ans=0
    for i in range(1,n+1):
        if x%i==0:
            ans+=1
            if i!=x//i:
                ans+=1
    return ans

t=int(input().strip())
for _ in range(t):
    x,y=map(int,input().strip().split())
    z=abs(x-y)
    
    example=[-1]*y+[1]*x
    
    print(cnt(z)%mod)
    print(*example)