import sys

data=sys.stdin.read().split() 
n=int(data[0])
a=[int(x) for x in data[1:]]

dp=[0]*32
for i in range(n):
    max_len=0

    for bit in range(31):
        if (a[i]>>bit)&1:
            if dp[bit]>max_len:
                max_len=dp[bit]

    new_len=max_len+1

    for bit in range(31):
        if (a[i]>>bit)&1:
            dp[bit]=new_len

print(max(dp))