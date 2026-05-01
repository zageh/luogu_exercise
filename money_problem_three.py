import sys
input=sys.stdin.readline

n,w=map(int,input().split())
a=list(map(int,input().split()))
mod=10**9+7

dp=[0]*(w+1)
dp[0]=1
for x in a:
    for i in range(x,w+1):
        dp[i]=(dp[i]+dp[i-x])%mod

print(dp[w])
#和二的区别主要是这是组合数，二是排列数
#这里的外层是面额，在用完一种面额的纸币后不会再回头用同种面额的纸币了，所以算出的取法是不区分取钱顺序的