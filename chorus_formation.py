import sys
input=sys.stdin.readline

n=int(input().strip())
t=list(map(int,input().split()))

inc=[1]*n
dec=[1]*n

for i in range(n):
    for j in range(i):
        if t[i]>t[j]:
            inc[i]=max(inc[i],inc[j]+1)

for i in range(n-1,-1,-1):
    for j in range(n-1,i,-1):
        if t[i]>t[j]:
            dec[i]=max(dec[i],dec[j]+1)

best=0
for i in range(n):
    best=max(best,inc[i]+dec[i]-1)

print(n-best)