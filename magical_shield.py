import sys

data=sys.stdin.read().split()

n=int(data[0])
c=int(data[1])
b=int(data[2])

s=[int(x) for x in data[3:3+n]]
a=[int(x) for x in data[3+n:]]

dp=[-1]*(n+1)
dp[0]=b
for i in range(n):
    for j in range(i+1,-1,-1):
        best=-1

        if j<=i and dp[j]!=-1:
            x=min(dp[j]+s[i],c)
            if x>=a[i]:
                best=x

        if s[i]>0 and j>0 and dp[j-1]!=-1:
            x=min(dp[j-1]+2*s[i],c)
            if x>=a[i]:
                best=max(best,x)

        dp[j]=best
            
i=0
while i<=n and dp[i]==-1:
    i+=1

if i <=n:
    print(i)
else:
    print(-1)