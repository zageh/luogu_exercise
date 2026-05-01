import sys
input=sys.stdin.readline

mod=676767677
t=int(input().strip())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    
    ans=0
    if a[-1]==1:
        ans=1
        
    for x in a:
        if x>1:
            ans+=x
            
    print(ans%mod)