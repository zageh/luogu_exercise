import sys

data=sys.stdin.read().split()

n=int(data[0])
m=int(data[1])
l=[int(x) for x in data[2:2+n]]
p=[0.0]+[float(x) for x in data[2+n:]]
pre=[0.0]*(m+1)
for i in range(1,m+1):
    pre[i]=pre[i-1]+p[i]

dp=[[0.0]*(m+1) for _ in range(1<<n)]
            
for mask in range(1<<n):
    for i in range(1,m+1):
        dp[mask][i]=dp[mask][i-1]
        
        for j in range(n):
            if (mask>>j)&1:
                pre_p=max(i-l[j],0)
                pre_m=mask^(1<<j)
                
                new=dp[pre_m][pre_p]+(pre[i]-pre[pre_p])
                
                if new>dp[mask][i]:
                    dp[mask][i]=new
                    
ans=pre[m]-dp[(1<<n)-1][m]
print(f"{ans:.2f}")   