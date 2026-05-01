import sys

data=sys.stdin.read().split()

n=int(data[0])
m=int(data[1])
l=int(data[2])
t=[int(x) for x in data[3:]]

t.sort()

s=t[-1]//n

p=[0]*(s+1)

for x in t:
    p[x//n]+=1

cnt=0
for x in p:
    cnt+=min(m,x)

print(cnt)