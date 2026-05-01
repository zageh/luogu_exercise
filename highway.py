import sys

data=sys.stdin.read().split()

n=int(data[0])
d=int(data[1])
v=[int(x) for x in data[2:n+1]]
a=[int(x) for x in data[n+1:]]

l=0
cost=0
last=0
mn=a[0]
for i in range(n-1):
    l+=v[i]
    if a[i+1]<mn or i==n-2:
        need=l//d
        if l%d!=0:
            need+=1
        cost+=(need-last)*mn
        mn=a[i+1]
        last=need

print(cost)