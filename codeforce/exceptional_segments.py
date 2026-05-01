import sys
input=sys.stdin.readline

mod=998244353

t=int(input())
for _ in range(t):
    n,x=map(int,input().split())
    l0,l1,r0,r1=0,0,0,0
    
    l0=(x//4+1)%mod
    r0=((n+1)//4-x//4)%mod
    
    l1=((x+2)//4)%mod
    r1=((n+3)//4-(x+2)//4)%mod

    print((l0*r0+l1*r1)%mod)