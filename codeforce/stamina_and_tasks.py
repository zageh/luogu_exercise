import sys
input=sys.stdin.readline

t=int(input())
for _ in range(t):
    n=int(input().strip())
    lst=[]
    for d in range(n):
        c,p=map(int,input().split())
        lst.append((c,p))
    s=1
    dp=[0]*(n+1)
    
    for i in range(n-1,-1,-1):
        dp[i]=max(dp[i+1],lst[i][0]+(1-lst[i][1]/100)*dp[i+1])
        
    print(f"{dp[0]:.10f}")